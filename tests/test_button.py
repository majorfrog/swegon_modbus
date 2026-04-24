"""Button platform tests."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
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
from custom_components.swegon_modbus.models import BUTTON_DESCRIPTIONS

from .fixtures import mock_error_result


@pytest.fixture
def platforms() -> list[Platform]:
    """Load only the button platform for this test module."""
    return [Platform.BUTTON]


_BUTTON_DESC = BUTTON_DESCRIPTIONS[0]


# ---------------------------------------------------------------------------
# Entity creation
# ---------------------------------------------------------------------------


async def test_button_entity_created(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration,
) -> None:
    """Button entity is registered after integration setup."""
    ent_reg = er.async_get(hass)
    entry = ent_reg.async_get_entity_id(
        "button",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_{_BUTTON_DESC.key}",
    )
    assert entry is not None


# ---------------------------------------------------------------------------
# async_press — happy path
# ---------------------------------------------------------------------------


async def test_button_press_writes_configured_value(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """Pressing the button writes the configured write_value to the register."""
    mock_client = setup_integration

    ent_reg = er.async_get(hass)
    entity_id = ent_reg.async_get_entity_id(
        "button",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_{_BUTTON_DESC.key}",
    )
    assert entity_id is not None

    mock_client.write_register.reset_mock()
    await hass.services.async_call(
        "button", "press", {"entity_id": entity_id}, blocking=True
    )
    await hass.async_block_till_done()

    mock_client.write_register.assert_called_once()
    call_kwargs = mock_client.write_register.call_args.kwargs
    assert call_kwargs["value"] == _BUTTON_DESC.write_value
    assert call_kwargs["address"] == _BUTTON_DESC.address


# ---------------------------------------------------------------------------
# async_press — write error propagates
# ---------------------------------------------------------------------------


async def test_button_press_raises_on_write_error(
    hass: HomeAssistant,
    mock_rtu_config_entry,
    setup_integration: MagicMock,
) -> None:
    """A Modbus write error on button press is surfaced as a HomeAssistantError."""
    mock_client = setup_integration
    mock_client.write_register = AsyncMock(return_value=mock_error_result())

    ent_reg = er.async_get(hass)
    entity_id = ent_reg.async_get_entity_id(
        "button",
        DOMAIN,
        f"{mock_rtu_config_entry.entry_id}_{_BUTTON_DESC.key}",
    )
    assert entity_id is not None

    with pytest.raises(HomeAssistantError):
        await hass.services.async_call(
            "button", "press", {"entity_id": entity_id}, blocking=True
        )


# ---------------------------------------------------------------------------
# Snapshot test — all button entities
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("entity_registry_enabled_by_default")
async def test_entities(
    hass: HomeAssistant,
    snapshot: SnapshotAssertion,
    entity_registry: EntityRegistry,
    init_integration: MockConfigEntry,
) -> None:
    """Verify all button entity states and attributes match the snapshot."""
    await snapshot_platform(hass, entity_registry, snapshot, init_integration.entry_id)
