"""Diagnostics support for the Swegon Modbus integration."""

from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.const import CONF_PORT
from homeassistant.core import HomeAssistant

from . import SwegonModbusConfigEntry

# Redact connection details that could expose the local environment.
TO_REDACT: set[str] = {CONF_PORT}


async def async_get_config_entry_diagnostics(
    _hass: HomeAssistant, entry: SwegonModbusConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator = entry.runtime_data
    return {
        "entry_data": async_redact_data(dict(entry.data), TO_REDACT),
        "coordinator": {
            "update_interval": str(coordinator.update_interval),
            "last_update_success": coordinator.last_update_success,
            "consecutive_failures": coordinator.consecutive_failures,
        },
        "data": dict(coordinator.data or {}),
    }
