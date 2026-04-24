"""Config flow for the Swegon Modbus integration."""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Self

from pymodbus.client import AsyncModbusSerialClient
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_PORT
from homeassistant.helpers.selector import (
    NumberSelector,
    NumberSelectorConfig,
    NumberSelectorMode,
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)

from .const import (
    CONF_BAUDRATE,
    CONF_BYTESIZE,
    CONF_PARITY,
    CONF_UNIT_ID,
    CONF_STOPBITS,
    DEFAULT_BAUDRATE,
    DEFAULT_BYTESIZE,
    DEFAULT_PARITY,
    DEFAULT_UNIT_ID,
    DEFAULT_STOPBITS,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


class SwegonModbusConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Swegon Modbus."""

    VERSION = 1
    MINOR_VERSION = 1

    def is_matching(self, other_flow: Self) -> bool:
        """Return False — duplicate detection is handled via unique IDs."""
        return False

    @staticmethod
    def _rtu_schema(defaults: dict[str, Any] | None = None) -> vol.Schema:
        """Build the RTU connection form schema."""
        d = defaults or {}
        return vol.Schema(
            {
                vol.Required(
                    CONF_PORT, default=d.get(CONF_PORT, vol.UNDEFINED)
                ): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required(
                    CONF_UNIT_ID, default=d.get(CONF_UNIT_ID, DEFAULT_UNIT_ID)
                ): NumberSelector(
                    NumberSelectorConfig(
                        min=1, max=247, step=1, mode=NumberSelectorMode.BOX
                    )
                ),
                vol.Required(
                    CONF_BAUDRATE, default=d.get(CONF_BAUDRATE, DEFAULT_BAUDRATE)
                ): NumberSelector(
                    NumberSelectorConfig(
                        min=300, max=115200, step=1, mode=NumberSelectorMode.BOX
                    )
                ),
                vol.Required(
                    CONF_BYTESIZE, default=d.get(CONF_BYTESIZE, DEFAULT_BYTESIZE)
                ): NumberSelector(
                    NumberSelectorConfig(
                        min=5, max=8, step=1, mode=NumberSelectorMode.BOX
                    )
                ),
                vol.Required(
                    CONF_PARITY, default=d.get(CONF_PARITY, DEFAULT_PARITY)
                ): SelectSelector(
                    SelectSelectorConfig(
                        options=[
                            SelectOptionDict(value="N", label="None"),
                            SelectOptionDict(value="E", label="Even"),
                            SelectOptionDict(value="O", label="Odd"),
                        ],
                        mode=SelectSelectorMode.LIST,
                    )
                ),
                vol.Required(
                    CONF_STOPBITS,
                    default=str(d.get(CONF_STOPBITS, DEFAULT_STOPBITS)),
                ): SelectSelector(
                    SelectSelectorConfig(
                        options=[
                            SelectOptionDict(value="1", label="1"),
                            SelectOptionDict(value="2", label="2"),
                        ],
                        mode=SelectSelectorMode.LIST,
                    )
                ),
            }
        )

    @staticmethod
    async def _async_test_rtu_connection(user_input: dict[str, Any]) -> dict[str, str]:
        """Test an RTU connection. Return error dict (empty if successful)."""
        client = AsyncModbusSerialClient(
            port=user_input[CONF_PORT],
            baudrate=int(user_input[CONF_BAUDRATE]),
            bytesize=int(user_input[CONF_BYTESIZE]),
            parity=user_input[CONF_PARITY],
            stopbits=int(user_input[CONF_STOPBITS]),
        )
        try:
            connected = await asyncio.wait_for(client.connect(), timeout=10.0)
        except (asyncio.TimeoutError, OSError):
            connected = False
            _LOGGER.debug("RTU connection test failed", exc_info=True)
        except Exception:  # noqa: BLE001
            connected = False
            _LOGGER.debug("RTU connection test failed", exc_info=True)
        else:
            if not connected:
                _LOGGER.debug("RTU connection test failed (connection returned False)")
        finally:
            client.close()

        return {} if connected else {"base": "cannot_connect"}

    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult:
        """Create a config entry from a configuration.yaml entry."""
        port = import_data[CONF_PORT]
        unit_id = import_data.get(CONF_UNIT_ID, DEFAULT_UNIT_ID)
        unique_id = f"rtu_{str(port).replace('/', '_')}_{unit_id}"
        data = {
            CONF_PORT: port,
            CONF_UNIT_ID: unit_id,
            CONF_BAUDRATE: import_data.get(CONF_BAUDRATE, DEFAULT_BAUDRATE),
            CONF_BYTESIZE: import_data.get(CONF_BYTESIZE, DEFAULT_BYTESIZE),
            CONF_PARITY: import_data.get(CONF_PARITY, DEFAULT_PARITY),
            CONF_STOPBITS: import_data.get(CONF_STOPBITS, DEFAULT_STOPBITS),
        }

        await self.async_set_unique_id(unique_id)
        self._abort_if_unique_id_configured()
        return self.async_create_entry(title=f"Swegon CASA RTU {port}", data=data)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Show the RTU serial connection form directly."""
        return await self.async_step_rtu(user_input)

    async def async_step_rtu(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Gather serial port settings; test the connection."""
        errors: dict[str, str] = {}

        if user_input is not None:
            errors = await self._async_test_rtu_connection(user_input)

            if not errors:
                port = user_input[CONF_PORT]
                unit_id = int(user_input[CONF_UNIT_ID])
                unique_id = f"rtu_{str(port).replace('/', '_')}_{unit_id}"
                await self.async_set_unique_id(unique_id)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=f"Swegon CASA RTU {port}",
                    data={
                        CONF_PORT: port,
                        CONF_UNIT_ID: unit_id,
                        CONF_BAUDRATE: int(user_input[CONF_BAUDRATE]),
                        CONF_BYTESIZE: int(user_input[CONF_BYTESIZE]),
                        CONF_PARITY: user_input[CONF_PARITY],
                        CONF_STOPBITS: int(user_input[CONF_STOPBITS]),
                    },
                )

        return self.async_show_form(
            step_id="rtu",
            data_schema=self._rtu_schema(),
            errors=errors,
        )

    async def async_step_reconfigure(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Allow updating connection parameters for an existing entry."""
        entry = self._get_reconfigure_entry()
        errors: dict[str, str] = {}

        if user_input is not None:
            errors = await self._async_test_rtu_connection(user_input)

            if not errors:
                port_str = user_input[CONF_PORT]
                unit_id = int(user_input[CONF_UNIT_ID])
                new_unique_id = f"rtu_{port_str.replace('/', '_')}_{unit_id}"
                data_updates: dict[str, Any] = {
                    CONF_PORT: port_str,
                    CONF_UNIT_ID: unit_id,
                    CONF_BAUDRATE: int(user_input[CONF_BAUDRATE]),
                    CONF_BYTESIZE: int(user_input[CONF_BYTESIZE]),
                    CONF_PARITY: user_input[CONF_PARITY],
                    CONF_STOPBITS: int(user_input[CONF_STOPBITS]),
                }
                return self.async_update_reload_and_abort(
                    entry,
                    unique_id=new_unique_id,
                    data_updates=data_updates,
                )

        return self.async_show_form(
            step_id="reconfigure",
            data_schema=self._rtu_schema(dict(entry.data)),
            errors=errors,
        )
