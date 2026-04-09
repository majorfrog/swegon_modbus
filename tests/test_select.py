"""Select platform tests."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import entity_registry as er

from custom_components.swegon_modbus.const import DOMAIN
from custom_components.swegon_modbus.models import SELECT_DESCRIPTIONS

from .fixtures import mock_error_result, mock_register_result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _entity_id(hass: HomeAssistant, entry_id: str, key: str) -> str | None:
    """Look up entity_id via unique_id."""
    return er.async_get(hass).async_get_entity_id("select", DOMAIN, f"{entry_id}_{key}")


# Pick the first select description to use for generic tests
_FIRST_SELECT = SELECT_DESCRIPTIONS[0]


# ---------------------------------------------------------------------------
# Entity creation
# ---------------------------------------------------------------------------


async def test_select_entity_created(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """First select entity is registered after integration setup."""
    assert (
        _entity_id(hass, mock_rtu_config_entry.entry_id, _FIRST_SELECT.key) is not None
    )


# ---------------------------------------------------------------------------
# current_option — mapped value
# ---------------------------------------------------------------------------


async def test_select_current_option_mapped(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    mock_rtu_client: MagicMock,
) -> None:
    """Select shows the mapped option for the raw register value."""
    mock_rtu_client.read_input_registers = AsyncMock(
        side_effect=lambda **kw: mock_register_result(value=0, count=kw.get("count", 1))
    )
    mock_rtu_client.read_holding_registers = AsyncMock(
        side_effect=lambda **kw: mock_register_result(value=0, count=kw.get("count", 1))
    )
    mock_rtu_client.write_register = AsyncMock(
        return_value=mock_register_result(value=0)
    )
    mock_rtu_config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(mock_rtu_config_entry.entry_id)
    await hass.async_block_till_done()
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, _FIRST_SELECT.key)
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    expected = _FIRST_SELECT.value_map[0]
    assert state.state == expected


# ---------------------------------------------------------------------------
# async_select_option — valid option
# ---------------------------------------------------------------------------


async def test_select_option_writes_raw_value(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """Selecting a valid option writes the corresponding raw int to the register."""
    mock_client = setup_integration
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, _FIRST_SELECT.key)
    assert entity_id is not None

    raw_key, option_string = next(iter(_FIRST_SELECT.value_map.items()))

    mock_client.write_register.reset_mock()
    await hass.services.async_call(
        "select",
        "select_option",
        {"entity_id": entity_id, "option": option_string},
        blocking=True,
    )
    await hass.async_block_till_done()

    mock_client.write_register.assert_called_once()
    call_kwargs = mock_client.write_register.call_args.kwargs
    assert call_kwargs["value"] == raw_key


# ---------------------------------------------------------------------------
# async_select_option — write error propagates as HomeAssistantError
# ---------------------------------------------------------------------------


async def test_select_write_error_raises(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """A Modbus write error is surfaced as a HomeAssistantError."""
    mock_client = setup_integration
    mock_client.write_register = AsyncMock(return_value=mock_error_result())
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, _FIRST_SELECT.key)
    assert entity_id is not None

    _, option_string = next(iter(_FIRST_SELECT.value_map.items()))

    with pytest.raises(HomeAssistantError):
        await hass.services.async_call(
            "select",
            "select_option",
            {"entity_id": entity_id, "option": option_string},
            blocking=True,
        )
