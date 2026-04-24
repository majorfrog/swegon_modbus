"""Data update coordinator for the Swegon Modbus integration."""

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from datetime import timedelta
import logging
import struct
from typing import TYPE_CHECKING, Any

from pymodbus.client import AsyncModbusSerialClient
from pymodbus.exceptions import ConnectionException, ModbusException

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PORT
from homeassistant.core import Event, HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    CONF_BAUDRATE,
    CONF_BYTESIZE,
    CONF_PARITY,
    CONF_UNIT_ID,
    CONF_STOPBITS,
    DATA_TYPE_ASCII,
    DATA_TYPE_FLOAT32,
    DATA_TYPE_INT16,
    DATA_TYPE_INT32,
    DATA_TYPE_UINT16,
    DATA_TYPE_UINT32,
    DOMAIN,
    INPUT_TYPE_INPUT,
    SCAN_INTERVAL_SECONDS,
)
from .models import (
    BINARY_SENSOR_DESCRIPTIONS,
    BUTTON_DESCRIPTIONS,
    COMBINED_SENSOR_DESCRIPTIONS,
    NUMBER_DESCRIPTIONS,
    SELECT_DESCRIPTIONS,
    SENSOR_DESCRIPTIONS,
    SWITCH_DESCRIPTIONS,
    ModbusSensorEntityDescription,
)

if TYPE_CHECKING:
    from . import SwegonModbusConfigEntry

_LOGGER = logging.getLogger(__name__)


def _decode_registers(registers: list[int], data_type: str) -> int | float:
    """Convert raw Modbus register value(s) to the appropriate Python type."""
    if data_type == DATA_TYPE_INT16:
        (raw_value,) = struct.unpack(">h", struct.pack(">H", registers[0]))
        return int(raw_value)
    if data_type == DATA_TYPE_UINT16:
        return registers[0]
    if data_type in (DATA_TYPE_INT32, DATA_TYPE_UINT32, DATA_TYPE_FLOAT32):
        if len(registers) < 2:
            raise ValueError(f"Need 2 registers for {data_type}, got {len(registers)}")
        raw = (registers[0] << 16) | registers[1]
        if data_type == DATA_TYPE_INT32:
            (raw_value,) = struct.unpack(">i", struct.pack(">I", raw))
            return int(raw_value)
        if data_type == DATA_TYPE_UINT32:
            return raw
        (raw_value,) = struct.unpack(">f", struct.pack(">I", raw))
        return float(raw_value)
    raise ValueError(f"Unsupported data_type: {data_type!r}")


def _decode_ascii_register(register: int) -> str:
    """Decode a single 16-bit Modbus register as two packed ASCII bytes.

    The high byte is the first character, the low byte is the second.
    Only printable ASCII characters (0x20–0x7E) are included; null bytes
    and non-printable characters are dropped.
    """
    high = (register >> 8) & 0xFF
    low = register & 0xFF
    return "".join(chr(b) for b in (high, low) if 0x20 <= b <= 0x7E)


def _register_count(data_type: str) -> int:
    """Return how many 16-bit registers a data type occupies."""
    if data_type in (DATA_TYPE_INT32, DATA_TYPE_UINT32, DATA_TYPE_FLOAT32):
        return 2
    return 1


class SwegonModbusCoordinator(DataUpdateCoordinator[dict[str, float | str | None]]):
    """Coordinator that polls a Modbus device for all defined sensors."""

    def __init__(
        self, hass: HomeAssistant, config_entry: SwegonModbusConfigEntry
    ) -> None:
        """Initialise the coordinator and create the appropriate Modbus client."""
        self._base_update_interval = timedelta(seconds=SCAN_INTERVAL_SECONDS)
        self._consecutive_failures: int = 0
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=self._base_update_interval,
            config_entry=config_entry,
        )
        self._client = self._build_client(config_entry.data)
        self._device_id: int = config_entry.data[CONF_UNIT_ID]
        self._modbus_lock = asyncio.Lock()

        self._enabled_keys: set[str] | None = None

        config_entry.async_on_unload(
            hass.bus.async_listen(
                er.EVENT_ENTITY_REGISTRY_UPDATED,
                self._handle_entity_registry_update,
            )
        )

    @property
    def consecutive_failures(self) -> int:
        """Return the number of consecutive update failures."""
        return self._consecutive_failures

    @callback
    def _handle_entity_registry_update(self, _event: Event) -> None:
        """Invalidate the enabled-keys cache when the entity registry changes."""
        self._enabled_keys = None

    def _get_enabled_keys(self) -> set[str]:
        """Return the cached set of enabled entity keys, rebuilding if stale."""
        if self._enabled_keys is not None:
            return self._enabled_keys

        registry = er.async_get(self.hass)
        prefix = f"{self.config_entry.entry_id}_"
        registry_entries = er.async_entries_for_config_entry(
            registry, self.config_entry.entry_id
        )
        if registry_entries:
            self._enabled_keys = {
                entry.unique_id[len(prefix) :]
                for entry in registry_entries
                if not entry.disabled
            }
        else:
            # On first boot, the entity registry is empty. In this case, we poll
            # all entities that have entity_registry_enabled_default=True, while
            # skipping those explicitly disabled by the integration.
            self._enabled_keys = {
                desc.key
                for desc in (
                    *SENSOR_DESCRIPTIONS,
                    *BINARY_SENSOR_DESCRIPTIONS,
                    *COMBINED_SENSOR_DESCRIPTIONS,
                    *SWITCH_DESCRIPTIONS,
                    *SELECT_DESCRIPTIONS,
                    *NUMBER_DESCRIPTIONS,
                    *BUTTON_DESCRIPTIONS,
                )
                if desc.entity_registry_enabled_default
            }
        return self._enabled_keys

    async def _read_batched(
        self,
        requests: list[tuple[str, int, str, str]],
    ) -> dict[int, int | None]:
        """Read a set of (key, address, data_type, input_type) requests in batches."""
        if not requests:
            return {}

        by_type: dict[str, list[tuple[str, int]]] = {}
        for key, address, _data_type, input_type in requests:
            by_type.setdefault(input_type, []).append((key, address))

        result: dict[int, int | None] = {}

        for input_type, items in by_type.items():
            items.sort(key=lambda x: x[1])

            runs: list[tuple[int, int]] = []
            for _key, addr in items:
                if runs and addr <= runs[-1][1] + 1:
                    runs[-1] = (runs[-1][0], max(runs[-1][1], addr))
                else:
                    runs.append((addr, addr))

            _LOGGER.debug(
                "_read_batched: input_type=%s, %d items → %d register run(s)",
                input_type,
                len(items),
                len(runs),
            )
            run_registers: dict[tuple[int, int], list[int] | None] = {}
            for start, end in runs:
                count = end - start + 1
                _LOGGER.debug(
                    "Reading registers [%d..%d] (count=%d, type=%s)",
                    start,
                    end,
                    count,
                    input_type,
                )
                regs = await self._read_registers(
                    f"batch_{start}_{end}", start, count, input_type
                )
                run_registers[(start, end)] = regs

            for _key, addr in items:
                reg_list = None
                for (start, end), regs in run_registers.items():
                    if start <= addr <= end and regs is not None:
                        reg_list = regs
                        offset = addr - start
                        break
                if reg_list is None:
                    result[addr] = None
                else:
                    result[addr] = reg_list[offset]

        return result

    @staticmethod
    def _build_client(
        data: Mapping[str, Any],
    ) -> AsyncModbusSerialClient:
        """Instantiate the Modbus RTU serial transport from config entry data."""
        return AsyncModbusSerialClient(
            port=data[CONF_PORT],
            baudrate=data[CONF_BAUDRATE],
            bytesize=data[CONF_BYTESIZE],
            parity=data[CONF_PARITY],
            stopbits=data[CONF_STOPBITS],
            timeout=3,
        )

    async def _read_registers(
        self,
        key: str,
        address: int,
        count: int,
        input_type: str,
    ) -> list[int] | None:
        """Perform the raw Modbus read and return register list, or None on error."""
        try:
            try:
                async with self._modbus_lock:
                    if input_type == INPUT_TYPE_INPUT:
                        result = await self._client.read_input_registers(
                            address=address,
                            count=count,
                            device_id=self._device_id,
                        )
                    else:
                        result = await self._client.read_holding_registers(
                            address=address,
                            count=count,
                            device_id=self._device_id,
                        )
            except ConnectionException:
                raise
            except ModbusException as err:
                _LOGGER.warning(
                    "Modbus protocol error reading %s (address %d): %s",
                    key,
                    address,
                    err,
                )
                return None

            if result.isError():
                _LOGGER.warning(
                    "Device returned error response for %s (address %d): %s",
                    key,
                    address,
                    result,
                )
                return None

            if not result.registers:
                _LOGGER.warning("Empty register data for %s (address %d)", key, address)
                return None

            return result.registers
        except asyncio.CancelledError:
            # Task was cancelled; close the client and re-raise so the coordinator
            # can properly handle the cancellation.
            self._client.close()
            raise

    async def _read_sensor(
        self, desc: ModbusSensorEntityDescription
    ) -> float | str | None:
        """Read a single sensor register and decode the value.

        For DATA_TYPE_ASCII sensors with register_count > 1 this reads a
        contiguous block of registers and decodes them as packed ASCII bytes.
        """
        if desc.data_type == DATA_TYPE_ASCII:
            registers = await self._read_registers(
                desc.key, desc.address, desc.register_count, desc.input_type
            )
            if registers is None:
                return None
            chars: list[str] = []
            for reg in registers:
                chars.append(_decode_ascii_register(reg))
            result = "".join(chars).strip()
            _LOGGER.debug(
                "Read ASCII %s (address %d, %d regs): %r",
                desc.key,
                desc.address,
                desc.register_count,
                result,
            )
            return result or None
        count = _register_count(desc.data_type)
        registers = await self._read_registers(
            desc.key, desc.address, count, desc.input_type
        )
        if registers is None:
            return None
        raw = _decode_registers(registers, desc.data_type)
        value = round(raw * desc.scale, desc.precision)
        _LOGGER.debug(
            "Read %s (address %d): raw=%s → %s %s",
            desc.key,
            desc.address,
            raw,
            value,
            desc.native_unit_of_measurement,
        )
        return value

    async def _read_register_int(
        self,
        key: str,
        address: int,
        data_type: str,
        input_type: str,
    ) -> int | None:
        """Read a register and return the raw integer value (no scaling)."""
        count = _register_count(data_type)
        registers = await self._read_registers(key, address, count, input_type)
        if registers is None:
            return None
        raw = int(_decode_registers(registers, data_type))
        _LOGGER.debug("Read raw %s (address %d): %d", key, address, raw)
        return raw

    def _apply_backoff(self) -> None:
        """Double the update interval on failure, capped at 32× the base."""
        self._consecutive_failures += 1
        new_interval = min(
            self._base_update_interval * (2**self._consecutive_failures),
            self._base_update_interval * 32,
        )
        self.update_interval = new_interval
        _LOGGER.debug(
            "Connection failed (attempt %d); retrying in %s",
            self._consecutive_failures,
            new_interval,
        )

    @callback
    def async_disconnect(self) -> None:
        """Close the Modbus transport; called on entry unload."""
        self._client.close()

    async def write_holding_register(
        self,
        address: int,
        value: int,
        min_raw: int | None = None,
        max_raw: int | None = None,
    ) -> None:
        """Write a single value to a holding register using FC6."""
        if min_raw is not None and value < min_raw:
            raise HomeAssistantError(
                translation_domain=DOMAIN,
                translation_key="value_out_of_range",
            )
        if max_raw is not None and value > max_raw:
            raise HomeAssistantError(
                translation_domain=DOMAIN,
                translation_key="value_out_of_range",
            )
        if value < 0:
            value = value & 0xFFFF
        async with self._modbus_lock:
            if not self._client.connected:
                try:
                    connected = await asyncio.wait_for(
                        self._client.connect(), timeout=10.0
                    )
                except (asyncio.TimeoutError, OSError):
                    connected = False
                if not connected:
                    raise HomeAssistantError(
                        translation_domain=DOMAIN,
                        translation_key="cannot_connect",
                    )
            result = await self._client.write_register(
                address=address,
                value=value,
                device_id=self._device_id,
            )
        if result.isError():
            raise HomeAssistantError(
                translation_domain=DOMAIN,
                translation_key="write_failed",
            )

    async def _async_update_data(self) -> dict[str, float | None]:
        """Fetch all sensor values from the Modbus device."""
        _LOGGER.debug(
            "_async_update_data started (connected=%s)", self._client.connected
        )
        if not self._client.connected:
            _LOGGER.debug("Not connected – attempting connect (timeout=10s)")
            try:
                connected = await asyncio.wait_for(self._client.connect(), timeout=10.0)
            except asyncio.TimeoutError:
                _LOGGER.debug("connect() timed out after 10 s")
                connected = False
            except OSError as err:
                _LOGGER.debug("connect() raised OSError: %s", err)
                connected = False
            if not connected:
                _LOGGER.debug("Connection failed; applying backoff")
                self._apply_backoff()
                raise UpdateFailed(
                    "Could not establish Modbus connection",
                    translation_domain=DOMAIN,
                    translation_key="cannot_connect",
                )
            _LOGGER.debug("Connected successfully")

        data: dict[str, float | str | None] = {}
        enabled_keys = self._get_enabled_keys()
        _LOGGER.debug("Polling %d enabled keys", len(enabled_keys))

        try:
            single_reg_sensors = [
                desc
                for desc in SENSOR_DESCRIPTIONS
                if desc.key in enabled_keys
                and _register_count(desc.data_type) == 1
                and desc.data_type != DATA_TYPE_ASCII
            ]
            multi_reg_sensors = [
                desc
                for desc in SENSOR_DESCRIPTIONS
                if desc.key in enabled_keys
                and (
                    _register_count(desc.data_type) > 1
                    or desc.data_type == DATA_TYPE_ASCII
                )
            ]

            _LOGGER.debug(
                "Reading %d single-register sensors, %d multi-register sensors",
                len(single_reg_sensors),
                len(multi_reg_sensors),
            )
            batched = await self._read_batched(
                [
                    (desc.key, desc.address, desc.data_type, desc.input_type)
                    for desc in single_reg_sensors
                ]
            )
            _LOGGER.debug("Single-register sensor batch complete")
            for desc in single_reg_sensors:
                raw_reg = batched.get(desc.address)
                if raw_reg is None:
                    data[desc.key] = None
                    continue
                raw = _decode_registers([raw_reg], desc.data_type)
                value = round(raw * desc.scale, desc.precision)
                _LOGGER.debug(
                    "Read %s (address %d): raw=%s → %s %s",
                    desc.key,
                    desc.address,
                    raw,
                    value,
                    desc.native_unit_of_measurement,
                )
                data[desc.key] = value

            for desc in multi_reg_sensors:
                _LOGGER.debug("Reading multi-register sensor: %s", desc.key)
                data[desc.key] = await self._read_sensor(desc)

            binary_enabled = [
                desc for desc in BINARY_SENSOR_DESCRIPTIONS if desc.key in enabled_keys
            ]
            _LOGGER.debug("Reading %d binary sensors", len(binary_enabled))
            binary_batched = await self._read_batched(
                [
                    (desc.key, desc.address, desc.data_type, desc.input_type)
                    for desc in binary_enabled
                ]
            )
            _LOGGER.debug("Binary sensor batch complete")
            raw_address_cache: dict[int, int | None] = {}
            for desc in binary_enabled:
                addr = desc.address
                if addr not in raw_address_cache:
                    raw_reg = binary_batched.get(addr)
                    if raw_reg is None:
                        raw_address_cache[addr] = None
                    else:
                        raw_address_cache[addr] = int(
                            _decode_registers([raw_reg], desc.data_type)
                        )
                raw = raw_address_cache[addr]
                if raw is None:
                    data[desc.key] = None
                elif desc.bit_position is not None:
                    data[desc.key] = float((raw >> desc.bit_position) & 1)
                else:
                    data[desc.key] = float(raw)

            for combined in COMBINED_SENSOR_DESCRIPTIONS:
                if combined.key not in enabled_keys:
                    continue
                for comp in combined.components:
                    if comp.key not in data:
                        data[comp.key] = await self._read_sensor(comp)

            writable_descs = [
                desc
                for desc in (
                    *SWITCH_DESCRIPTIONS,
                    *SELECT_DESCRIPTIONS,
                    *NUMBER_DESCRIPTIONS,
                )
                if desc.key in enabled_keys
            ]
            _LOGGER.debug(
                "Reading %d writable entities (switch/select/number)",
                len(writable_descs),
            )
            writable_batched = await self._read_batched(
                [
                    (desc.key, desc.address, desc.data_type, desc.input_type)
                    for desc in writable_descs
                ]
            )
            _LOGGER.debug("Writable entity batch complete")
            for desc in writable_descs:
                raw_reg = writable_batched.get(desc.address)
                if raw_reg is None:
                    data[desc.key] = None
                else:
                    raw = int(_decode_registers([raw_reg], desc.data_type))
                    _LOGGER.debug(
                        "Read raw %s (address %d): %d", desc.key, desc.address, raw
                    )
                    data[desc.key] = float(raw)

        except ConnectionException as err:
            self._apply_backoff()
            raise UpdateFailed(
                f"Modbus connection lost during poll: {err}",
                translation_domain=DOMAIN,
                translation_key="connection_lost",
                translation_placeholders={"error": str(err)},
            ) from err

        if self._consecutive_failures > 0:
            self._consecutive_failures = 0
            self.update_interval = self._base_update_interval

        _LOGGER.debug("_async_update_data complete, fetched %d values", len(data))
        return data
