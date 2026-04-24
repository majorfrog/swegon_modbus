"""Swegon Modbus integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, SOURCE_IMPORT
from homeassistant.const import CONF_PORT, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

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
from .coordinator import SwegonModbusCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
]

type SwegonModbusConfigEntry = ConfigEntry[SwegonModbusCoordinator]


_DEVICE_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_PORT): cv.string,
        vol.Optional(CONF_UNIT_ID, default=DEFAULT_UNIT_ID): vol.All(
            int, vol.Range(min=1, max=247)
        ),
        vol.Optional(CONF_BAUDRATE, default=DEFAULT_BAUDRATE): cv.positive_int,
        vol.Optional(CONF_BYTESIZE, default=DEFAULT_BYTESIZE): vol.In([5, 6, 7, 8]),
        vol.Optional(CONF_PARITY, default=DEFAULT_PARITY): vol.In(["N", "E", "O"]),
        vol.Optional(CONF_STOPBITS, default=DEFAULT_STOPBITS): vol.In([1, 2]),
    }
)

CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: vol.All(cv.ensure_list, [_DEVICE_SCHEMA])},
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """Import entries defined in configuration.yaml."""
    for device_config in config.get(DOMAIN, []):
        _LOGGER.debug("Scheduling import flow for device: %s", device_config)
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN,
                context={"source": SOURCE_IMPORT},
                data=device_config,
            )
        )
    return True


async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate old config entry versions to the current schema.

    Currently, the integration is at VERSION 1, so no migrations are needed.
    This function is a placeholder for future migrations when the config
    entry schema changes.
    """
    _LOGGER.debug("Migrating entry %s from version %s", entry.entry_id, entry.version)
    return True


async def async_setup_entry(
    hass: HomeAssistant, entry: SwegonModbusConfigEntry
) -> bool:
    """Set up Swegon Modbus from a config entry."""
    _LOGGER.debug("Setting up entry %s", entry.entry_id)
    coordinator = SwegonModbusCoordinator(hass, entry)

    _LOGGER.debug("Starting first refresh")
    await coordinator.async_config_entry_first_refresh()
    _LOGGER.debug("First refresh complete")

    entry.runtime_data = coordinator

    entry.async_on_unload(coordinator.async_disconnect)

    _LOGGER.debug("Forwarding entry setup to platforms: %s", PLATFORMS)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    _LOGGER.debug("Platform setup complete")
    return True


async def async_unload_entry(
    hass: HomeAssistant, entry: SwegonModbusConfigEntry
) -> bool:
    """Unload a Swegon Modbus config entry."""
    return bool(await hass.config_entries.async_unload_platforms(entry, PLATFORMS))
