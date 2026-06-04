"""__init__.py tests — covers YAML import, CONFIG_SCHEMA validation, async_setup."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

try:
    from pytest_homeassistant_custom_component.common import MockConfigEntry
except ImportError:
    from tests.common import MockConfigEntry  # type: ignore[no-redef]

from custom_components.swegon_modbus.const import DOMAIN

from .fixtures import MOCK_RTU_ENTRY_DATA


# ---------------------------------------------------------------------------
# CONFIG_SCHEMA validation — RTU
# ---------------------------------------------------------------------------


def test_validate_device_config_rtu_missing_port_raises() -> None:
    """CONFIG_SCHEMA raises vol.MultipleInvalid when RTU config is missing a port."""
    from custom_components.swegon_modbus import CONFIG_SCHEMA

    with pytest.raises(vol.MultipleInvalid):
        CONFIG_SCHEMA(
            {
                DOMAIN: [
                    {
                        # CONF_PORT intentionally omitted
                        "unit_id": 1,
                    }
                ]
            }
        )


def test_validate_device_config_valid_rtu_returns_config() -> None:
    """CONFIG_SCHEMA returns the processed config for a valid RTU entry."""
    from custom_components.swegon_modbus import CONFIG_SCHEMA
    from homeassistant.const import CONF_PORT

    result = CONFIG_SCHEMA({DOMAIN: [MOCK_RTU_ENTRY_DATA]})
    assert result[DOMAIN][0][CONF_PORT] == MOCK_RTU_ENTRY_DATA["port"]


# ---------------------------------------------------------------------------
# async_setup — iterates over YAML entries and calls async_init
# ---------------------------------------------------------------------------


async def test_async_setup_with_yaml_config_imports_entry(
    hass: HomeAssistant,
) -> None:
    """async_setup triggers a config-flow import for each entry in configuration.yaml."""
    from custom_components.swegon_modbus import async_setup

    result = await async_setup(hass, {DOMAIN: [MOCK_RTU_ENTRY_DATA]})

    assert result is True
    await hass.async_block_till_done()

    entries = hass.config_entries.async_entries(DOMAIN)
    flows = hass.config_entries.flow.async_progress_by_handler(DOMAIN)
    assert entries or flows, "Expected at least one config entry or in-progress flow"


async def test_async_setup_entry_refresh_failure_closes_client(
    hass: HomeAssistant,
) -> None:
    """Failed first refresh closes the client before re-raising."""
    from custom_components.swegon_modbus import async_setup_entry

    entry = MockConfigEntry(
        domain=DOMAIN,
        data=MOCK_RTU_ENTRY_DATA,
        title="Swegon CASA",
        unique_id="swegon_setup_fail",
    )
    entry.add_to_hass(hass)

    coordinator = MagicMock()
    coordinator.async_config_entry_first_refresh = AsyncMock(
        side_effect=ConfigEntryNotReady("connect failed")
    )
    coordinator.async_disconnect = MagicMock()

    with patch(
        "custom_components.swegon_modbus.SwegonModbusCoordinator",
        return_value=coordinator,
    ):
        with pytest.raises(ConfigEntryNotReady):
            await async_setup_entry(hass, entry)

    coordinator.async_disconnect.assert_called_once()


async def test_connection_exception_during_update_closes_client(
    hass: HomeAssistant,
) -> None:
    """Connection loss during poll closes the client to release serial lock."""
    from pymodbus.exceptions import ConnectionException

    from custom_components.swegon_modbus.coordinator import SwegonModbusCoordinator

    entry = MockConfigEntry(
        domain=DOMAIN,
        data=MOCK_RTU_ENTRY_DATA,
        title="Swegon CASA",
        unique_id="swegon_poll_fail",
    )
    entry.add_to_hass(hass)

    mock_client = MagicMock()
    mock_client.connected = True
    mock_client.close = MagicMock()
    mock_client.read_input_registers = AsyncMock(
        side_effect=ConnectionException("lost")
    )
    mock_client.read_holding_registers = AsyncMock(
        side_effect=ConnectionException("lost")
    )

    with patch(
        "custom_components.swegon_modbus.coordinator.AsyncModbusSerialClient",
        return_value=mock_client,
    ):
        coordinator = SwegonModbusCoordinator(hass, entry)

    from homeassistant.helpers.update_coordinator import UpdateFailed

    with pytest.raises(UpdateFailed, match="Modbus connection lost"):
        await coordinator._async_update_data()

    mock_client.close.assert_called_once()
