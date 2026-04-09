"""Number platform tests."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import entity_registry as er

from custom_components.swegon_modbus.const import DOMAIN
from custom_components.swegon_modbus.models import NUMBER_DESCRIPTIONS

from .fixtures import mock_error_result, mock_register_result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _entity_id(hass: HomeAssistant, entry_id: str, key: str) -> str | None:
    """Look up entity_id via unique_id."""
    return er.async_get(hass).async_get_entity_id("number", DOMAIN, f"{entry_id}_{key}")


# Use the first number description with a scale of 1.0 for simple integer tests
_DESC = next(d for d in NUMBER_DESCRIPTIONS if d.scale == 1.0)


# ---------------------------------------------------------------------------
# Entity creation
# ---------------------------------------------------------------------------


async def test_number_entity_created(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """First number entity is registered after integration setup."""
    assert _entity_id(hass, mock_rtu_config_entry.entry_id, _DESC.key) is not None


# ---------------------------------------------------------------------------
# native_value
# ---------------------------------------------------------------------------


async def test_number_native_value(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    mock_rtu_client: MagicMock,
) -> None:
    """Number reports the register value multiplied by the scale."""
    raw = 50
    mock_rtu_client.read_input_registers = AsyncMock(
        side_effect=lambda **kw: mock_register_result(
            value=raw, count=kw.get("count", 1)
        )
    )
    mock_rtu_client.read_holding_registers = AsyncMock(
        side_effect=lambda **kw: mock_register_result(
            value=raw, count=kw.get("count", 1)
        )
    )
    mock_rtu_client.write_register = AsyncMock(
        return_value=mock_register_result(value=raw)
    )
    mock_rtu_config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(mock_rtu_config_entry.entry_id)
    await hass.async_block_till_done()
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, _DESC.key)
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert float(state.state) == pytest.approx(raw * _DESC.scale)


# ---------------------------------------------------------------------------
# async_set_native_value
# ---------------------------------------------------------------------------


async def test_number_set_value_writes_scaled_raw(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """Setting a value writes round(value / scale) to the register."""
    mock_client = setup_integration
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, _DESC.key)
    assert entity_id is not None

    target = (_DESC.native_min_value + _DESC.native_max_value) / 2
    expected_raw = round(target / _DESC.scale)

    mock_client.write_register.reset_mock()
    await hass.services.async_call(
        "number", "set_value", {"entity_id": entity_id, "value": target}, blocking=True
    )
    await hass.async_block_till_done()

    mock_client.write_register.assert_called_once()
    call_kwargs = mock_client.write_register.call_args.kwargs
    assert call_kwargs["value"] == expected_raw


# ---------------------------------------------------------------------------
# async_set_native_value — write error propagates as HomeAssistantError
# ---------------------------------------------------------------------------


async def test_number_write_error_raises(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """A Modbus write error propagates as a HomeAssistantError."""
    mock_client = setup_integration
    mock_client.write_register = AsyncMock(return_value=mock_error_result())
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, _DESC.key)
    assert entity_id is not None

    target = (_DESC.native_min_value + _DESC.native_max_value) / 2

    with pytest.raises(HomeAssistantError):
        await hass.services.async_call(
            "number",
            "set_value",
            {"entity_id": entity_id, "value": target},
            blocking=True,
        )
