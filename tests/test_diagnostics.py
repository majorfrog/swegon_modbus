"""Diagnostics platform tests."""

from __future__ import annotations

from homeassistant.core import HomeAssistant

from custom_components.swegon_modbus.diagnostics import (
    async_get_config_entry_diagnostics,
)

from .fixtures import MOCK_UNIT_ID


# ---------------------------------------------------------------------------
# async_get_config_entry_diagnostics
# ---------------------------------------------------------------------------


async def test_diagnostics_contains_entry_data(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """Diagnostics output includes the config entry data with sensitive fields redacted."""
    result = await async_get_config_entry_diagnostics(hass, mock_rtu_config_entry)

    assert "entry_data" in result
    entry_data = result["entry_data"]
    # Port is redacted for privacy
    assert entry_data["port"] == "**REDACTED**"
    assert entry_data["unit_id"] == MOCK_UNIT_ID


async def test_diagnostics_contains_coordinator_stats(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """Diagnostics output includes coordinator update stats."""
    result = await async_get_config_entry_diagnostics(hass, mock_rtu_config_entry)

    assert "coordinator" in result
    coordinator = result["coordinator"]
    assert "update_interval" in coordinator
    assert "last_update_success" in coordinator
    assert "consecutive_failures" in coordinator
    assert coordinator["last_update_success"] is True
    assert coordinator["consecutive_failures"] == 0


async def test_diagnostics_contains_register_data(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """Diagnostics output includes the full data snapshot."""
    result = await async_get_config_entry_diagnostics(hass, mock_rtu_config_entry)

    assert "data" in result
    # fresh_air_temp should be present after a successful poll
    assert "fresh_air_temp" in result["data"]
