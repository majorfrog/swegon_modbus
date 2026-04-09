"""Button platform for the Swegon Modbus integration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .entity import SwegonModbusEntity, create_device_info
from .models import BUTTON_DESCRIPTIONS, ModbusButtonEntityDescription

if TYPE_CHECKING:
    from . import SwegonModbusConfigEntry
    from .coordinator import SwegonModbusCoordinator

PARALLEL_UPDATES = 1


async def async_setup_entry(
    _hass: HomeAssistant,
    entry: SwegonModbusConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Swegon Modbus button entities from a config entry."""
    coordinator: SwegonModbusCoordinator = entry.runtime_data
    async_add_entities(
        SwegonModbusButton(coordinator, description)
        for description in BUTTON_DESCRIPTIONS
    )


class SwegonModbusButton(SwegonModbusEntity, ButtonEntity):
    """Represents a Modbus holding register as a Home Assistant button."""

    def __init__(
        self,
        coordinator: SwegonModbusCoordinator,
        description: ModbusButtonEntityDescription,
    ) -> None:
        """Initialise the button."""
        super().__init__(coordinator)
        self.entity_description = description
        config_entry = coordinator.config_entry
        assert config_entry is not None
        self._attr_unique_id = f"{config_entry.entry_id}_{description.key}"
        self._attr_device_info = create_device_info(coordinator)

    async def async_press(self) -> None:
        """Write the trigger value to the holding register."""
        desc = self.entity_description
        await self.coordinator.write_holding_register(desc.address, desc.write_value)
        await self.coordinator.async_request_refresh()
