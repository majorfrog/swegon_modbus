"""Pytest fixtures for Swegon Modbus integration tests."""

from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

try:
    from pytest_homeassistant_custom_component.common import MockConfigEntry
    from pytest_homeassistant_custom_component.syrupy import (
        HomeAssistantSnapshotExtension,
    )
except ImportError:  # running inside the HA core test suite
    from tests.common import MockConfigEntry  # type: ignore[no-redef]
    from tests.syrupy import HomeAssistantSnapshotExtension  # type: ignore[no-redef]

from syrupy.assertion import SnapshotAssertion

from custom_components.swegon_modbus import PLATFORMS
from custom_components.swegon_modbus.const import DOMAIN

from .fixtures import (
    MOCK_RTU_ENTRY_DATA,
    mock_register_result,
)


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Automatically enable custom integrations in every test."""
    yield


@pytest.fixture
def snapshot(snapshot: SnapshotAssertion) -> SnapshotAssertion:
    """Return snapshot assertion using the Home Assistant extension."""
    return snapshot.use_extension(HomeAssistantSnapshotExtension)


@pytest.fixture
def entity_registry_enabled_by_default() -> Generator[None, None, None]:
    """Enable all entities in the entity registry for snapshot tests."""
    with patch(
        "homeassistant.helpers.entity.Entity.entity_registry_enabled_default",
        return_value=True,
    ):
        yield


@pytest.fixture
def platforms() -> list[Platform]:
    """Return the list of platforms to load; override per test module for isolation."""
    return PLATFORMS


@pytest.fixture
def mock_rtu_client() -> Generator[MagicMock, None, None]:
    """Patch AsyncModbusSerialClient used by the coordinator."""
    with patch(
        "custom_components.swegon_modbus.coordinator.AsyncModbusSerialClient"
    ) as mock_class:
        client = MagicMock()
        client.connected = True
        client.connect = AsyncMock(return_value=True)
        client.close = MagicMock()
        client.read_input_registers = AsyncMock(
            side_effect=lambda **kw: mock_register_result(count=kw.get("count", 1))
        )
        client.read_holding_registers = AsyncMock(
            side_effect=lambda **kw: mock_register_result(count=kw.get("count", 1))
        )
        client.write_register = AsyncMock(return_value=mock_register_result())
        mock_class.return_value = client
        yield client


@pytest.fixture
def mock_rtu_config_flow_client() -> Generator[MagicMock, None, None]:
    """Patch AsyncModbusSerialClient used only by the config flow connection test."""
    with patch(
        "custom_components.swegon_modbus.config_flow.AsyncModbusSerialClient"
    ) as mock_class:
        client = MagicMock()
        client.connect = AsyncMock(return_value=True)
        client.close = MagicMock()
        client.read_input_registers = AsyncMock(return_value=mock_register_result())
        mock_class.return_value = client
        yield client


@pytest.fixture
def mock_rtu_config_entry() -> MockConfigEntry:
    """Return a MockConfigEntry for an RTU connection."""
    return MockConfigEntry(
        domain=DOMAIN,
        data=MOCK_RTU_ENTRY_DATA,
        title=f"RTU {MOCK_RTU_ENTRY_DATA['port']} (unit {MOCK_RTU_ENTRY_DATA['unit_id']})",
        unique_id=(
            f"rtu_{MOCK_RTU_ENTRY_DATA['port'].replace('/', '_')}"
            f"_{MOCK_RTU_ENTRY_DATA['unit_id']}"
        ),
        entry_id="test_swegon_modbus_entry_id",
    )


@pytest.fixture
async def init_integration(
    hass: HomeAssistant,
    mock_rtu_config_entry: MockConfigEntry,
    mock_rtu_client: MagicMock,
    platforms: list[Platform],
) -> AsyncGenerator[MockConfigEntry, None]:
    """Set up the integration for testing, patching PLATFORMS for isolation."""
    mock_rtu_config_entry.add_to_hass(hass)
    with patch("custom_components.swegon_modbus.PLATFORMS", platforms):
        await hass.config_entries.async_setup(mock_rtu_config_entry.entry_id)
        await hass.async_block_till_done()
        yield mock_rtu_config_entry


@pytest.fixture
async def setup_integration(
    init_integration: MockConfigEntry,
) -> AsyncGenerator[MagicMock, None]:
    """Set up the integration and yield the mock Modbus client."""
    yield init_integration.runtime_data._client
