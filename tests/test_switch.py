"""Switch platform tests."""

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
    """Load only the switch platform for this test module."""
    return [Platform.SWITCH]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _entity_id(hass: HomeAssistant, entry_id: str, key: str) -> str | None:
    """Look up entity_id via unique_id."""
    return er.async_get(hass).async_get_entity_id("switch", DOMAIN, f"{entry_id}_{key}")


# ---------------------------------------------------------------------------
# Entity creation
# ---------------------------------------------------------------------------


async def test_switch_entity_created(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """travelling_mode switch entity is registered after integration setup."""
    assert (
        _entity_id(hass, mock_rtu_config_entry.entry_id, "travelling_mode") is not None
    )


# ---------------------------------------------------------------------------
# is_on
# ---------------------------------------------------------------------------


async def test_switch_is_on_when_register_nonzero(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """Switch reports ON when the holding register is non-zero."""
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, "travelling_mode")
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "on"


async def test_switch_is_off_when_register_zero(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    mock_rtu_client: MagicMock,
) -> None:
    """Switch reports OFF when the holding register is 0."""
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
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, "travelling_mode")
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "off"


# ---------------------------------------------------------------------------
# async_turn_on / async_turn_off
# ---------------------------------------------------------------------------


async def test_switch_turn_on_writes_one(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """Turning on writes 1 to the register."""
    mock_client = setup_integration
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, "travelling_mode")
    assert entity_id is not None

    mock_client.write_register.reset_mock()
    await hass.services.async_call(
        "switch", "turn_on", {"entity_id": entity_id}, blocking=True
    )
    await hass.async_block_till_done()

    mock_client.write_register.assert_called_once()
    call_kwargs = mock_client.write_register.call_args.kwargs
    assert call_kwargs["value"] == 1


async def test_switch_turn_off_writes_zero(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """Turning off writes 0 to the register."""
    mock_client = setup_integration
    entity_id = _entity_id(hass, mock_rtu_config_entry.entry_id, "travelling_mode")
    assert entity_id is not None

    mock_client.write_register.reset_mock()
    await hass.services.async_call(
        "switch", "turn_off", {"entity_id": entity_id}, blocking=True
    )
    await hass.async_block_till_done()

    mock_client.write_register.assert_called_once()
    call_kwargs = mock_client.write_register.call_args.kwargs
    assert call_kwargs["value"] == 0


# ---------------------------------------------------------------------------
# Snapshot test — all switch entities
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("entity_registry_enabled_by_default")
async def test_entities(
    hass: HomeAssistant,
    snapshot: SnapshotAssertion,
    entity_registry: EntityRegistry,
    init_integration: MockConfigEntry,
) -> None:
    """Verify all switch entity states and attributes match the snapshot."""
    await snapshot_platform(hass, entity_registry, snapshot, init_integration.entry_id)
