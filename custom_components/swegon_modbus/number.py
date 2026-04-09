"""Number platform for the Swegon Modbus integration."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

_LOGGER = logging.getLogger(__name__)

from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .entity import SwegonModbusEntity, create_device_info
from .models import NUMBER_DESCRIPTIONS, ModbusNumberEntityDescription

if TYPE_CHECKING:
    from . import SwegonModbusConfigEntry
    from .coordinator import SwegonModbusCoordinator

PARALLEL_UPDATES = 1


async def async_setup_entry(
    _hass: HomeAssistant,
    entry: SwegonModbusConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Swegon Modbus number entities from a config entry."""
    coordinator: SwegonModbusCoordinator = entry.runtime_data
    async_add_entities(
        SwegonModbusNumber(coordinator, description)
        for description in NUMBER_DESCRIPTIONS
    )


class SwegonModbusNumber(SwegonModbusEntity, NumberEntity):
    """Represents a Modbus holding register as a Home Assistant number."""

    def __init__(
        self,
        coordinator: SwegonModbusCoordinator,
        description: ModbusNumberEntityDescription,
    ) -> None:
        """Initialise the number entity."""
        super().__init__(coordinator)
        self.entity_description = description
        config_entry = coordinator.config_entry
        assert config_entry is not None
        self._attr_unique_id = f"{config_entry.entry_id}_{description.key}"
        self._attr_device_info = create_device_info(coordinator)
        self._attr_native_min_value = description.native_min_value
        self._attr_native_max_value = description.native_max_value
        self._attr_native_step = description.native_step
        self._attr_mode = description.mode

    @property
    def available(self) -> bool:
        """Return True when coordinator succeeded and the register has a value."""
        if not super().available:
            return False
        data = self.coordinator.data
        if data is None or data.get(self.entity_description.key) is None:
            return False
        condition = self.entity_description.available_when
        if condition and any(data.get(k) != v for k, v in condition.items()):
            return False
        return True

    @property
    def native_value(self) -> float | None:
        """Return the current value from coordinator data."""
        raw = self.coordinator.data.get(self.entity_description.key)
        if raw is None:
            return None
        return raw * self.entity_description.scale

    async def async_set_native_value(self, value: float) -> None:
        """Write a new value to the holding register."""
        desc = self.entity_description
        raw = round(value / desc.scale)
        min_raw = round(desc.native_min_value / desc.scale)
        max_raw = round(desc.native_max_value / desc.scale)
        await self.coordinator.write_holding_register(
            desc.address, raw, min_raw=min_raw, max_raw=max_raw
        )
        await self.coordinator.async_request_refresh()
