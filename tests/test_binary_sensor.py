"""Binary sensor platform tests."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity_registry import EntityRegistry
from syrupy.assertion import SnapshotAssertion

try:
    from pytest_homeassistant_custom_component.common import (
        MockConfigEntry,
        snapshot_platform,
    )
except ImportError:
    from tests.common import MockConfigEntry, snapshot_platform  # type: ignore[no-redef]

from custom_components.swegon_modbus.const import DOMAIN

from .fixtures import mock_register_result


@pytest.fixture
def platforms() -> list[Platform]:
    """Load only the binary_sensor platform for this test module."""
    return [Platform.BINARY_SENSOR]


# ---------------------------------------------------------------------------
# Entity creation
# ---------------------------------------------------------------------------


async def test_binary_sensor_entity_created(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """combined_alarm binary sensor entity is registered after integration setup."""
    ent_reg = er.async_get(hass)
    entry = ent_reg.async_get_entity_id(
        "binary_sensor",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_combined_alarm",
    )
    assert entry is not None


# ---------------------------------------------------------------------------
# is_on — whole-register sensor
# ---------------------------------------------------------------------------


async def test_binary_sensor_is_on_when_register_is_nonzero(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """combined_alarm is ON when the register value is non-zero."""
    # mock_register_result returns 215 by default — non-zero → ON
    ent_reg = er.async_get(hass)
    entity_id = ent_reg.async_get_entity_id(
        "binary_sensor",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_combined_alarm",
    )
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "on"


async def test_binary_sensor_is_off_when_register_is_zero(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    mock_rtu_client: MagicMock,
) -> None:
    """combined_alarm is OFF when the register value is zero."""
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

    ent_reg = er.async_get(hass)
    entity_id = ent_reg.async_get_entity_id(
        "binary_sensor",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_combined_alarm",
    )
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "off"


# ---------------------------------------------------------------------------
# Snapshot test — all binary_sensor entities
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("entity_registry_enabled_by_default")
async def test_entities(
    hass: HomeAssistant,
    snapshot: SnapshotAssertion,
    entity_registry: EntityRegistry,
    init_integration: MockConfigEntry,
) -> None:
    """Verify all binary_sensor entity states and attributes match the snapshot."""
    await snapshot_platform(hass, entity_registry, snapshot, init_integration.entry_id)
