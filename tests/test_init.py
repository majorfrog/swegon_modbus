"""__init__.py tests — covers YAML import, CONFIG_SCHEMA validation, async_setup."""

from __future__ import annotations

import pytest
import voluptuous as vol
from homeassistant.core import HomeAssistant

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
