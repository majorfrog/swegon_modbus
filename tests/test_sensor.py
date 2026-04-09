"""Sensor platform tests — covers sensor.py and __init__.py for Silver test-coverage."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity_registry import EntityRegistry
from pymodbus.exceptions import ConnectionException

from custom_components.swegon_modbus.const import DOMAIN

from .fixtures import MOCK_FRESH_AIR_TEMP_VALUE, mock_register_result


# ---------------------------------------------------------------------------
# Entity creation
# ---------------------------------------------------------------------------


async def test_sensor_entity_created(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    entity_registry: EntityRegistry,
    setup_integration,
) -> None:
    """fresh_air_temp sensor entity is registered after integration setup."""
    entry = entity_registry.async_get_entity_id(
        "sensor",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_fresh_air_temp",
    )
    assert entry is not None


# ---------------------------------------------------------------------------
# native_value — happy path
# ---------------------------------------------------------------------------


async def test_sensor_native_value(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """fresh_air_temp sensor reports the decoded register value."""
    ent_reg = er.async_get(hass)
    entry = ent_reg.async_get_entity_id(
        "sensor",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_fresh_air_temp",
    )
    assert entry is not None
    state = hass.states.get(entry)
    assert state is not None
    assert float(state.state) == pytest.approx(MOCK_FRESH_AIR_TEMP_VALUE)


# ---------------------------------------------------------------------------
# available — coordinator data is None
# ---------------------------------------------------------------------------


async def test_sensor_unavailable_when_coordinator_fails(
    hass: HomeAssistant,
    mock_rtu_config_entry,
) -> None:
    """Sensor is unavailable when coordinator raises UpdateFailed on first refresh."""
    mock_client = MagicMock()
    mock_client.connected = False
    mock_client.connect = AsyncMock(return_value=False)
    mock_client.close = MagicMock()

    with patch(
        "custom_components.swegon_modbus.coordinator.AsyncModbusSerialClient",
        return_value=mock_client,
    ):
        mock_rtu_config_entry.add_to_hass(hass)
        await hass.config_entries.async_setup(mock_rtu_config_entry.entry_id)
        await hass.async_block_till_done()

    from homeassistant.config_entries import ConfigEntryState

    assert (
        hass.config_entries.async_get_entry(mock_rtu_config_entry.entry_id).state
        == ConfigEntryState.SETUP_RETRY
    )


# ---------------------------------------------------------------------------
# ENUM sensor — unit_state mapped value
# ---------------------------------------------------------------------------


async def test_enum_sensor_shows_mapped_state(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    mock_rtu_client: MagicMock,
) -> None:
    """unit_state sensor shows a string state from the value_map."""
    # Return 3 for all registers → "normal"
    mock_rtu_client.read_input_registers = AsyncMock(
        side_effect=lambda **kw: mock_register_result(value=3, count=kw.get("count", 1))
    )
    mock_rtu_client.read_holding_registers = AsyncMock(
        side_effect=lambda **kw: mock_register_result(value=3, count=kw.get("count", 1))
    )
    mock_rtu_client.write_register = AsyncMock(
        return_value=mock_register_result(value=3)
    )
    mock_rtu_config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(mock_rtu_config_entry.entry_id)
    await hass.async_block_till_done()

    ent_reg = er.async_get(hass)
    entity_id = ent_reg.async_get_entity_id(
        "sensor",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_unit_state",
    )
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "normal"
