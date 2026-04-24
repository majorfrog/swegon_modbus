"""Base entity class for the Swegon Modbus integration."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER, MODEL

if TYPE_CHECKING:
    from .coordinator import SwegonModbusCoordinator

_LOGGER = logging.getLogger(__name__)


def create_device_info(coordinator: SwegonModbusCoordinator) -> DeviceInfo:
    """Build the DeviceInfo dict for this coordinator's device."""
    entry = coordinator.config_entry
    if entry is None:
        raise RuntimeError(
            "create_device_info called before coordinator was bound to a config entry"
        )
    return DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=MODEL,
        manufacturer=MANUFACTURER,
        model=MODEL,
    )


class SwegonModbusEntity(CoordinatorEntity["SwegonModbusCoordinator"]):
    """Base class shared by all Swegon Modbus entity platforms."""

    _attr_has_entity_name = True

    @property
    def suggested_object_id(self) -> str | None:
        """Use the register key as the entity ID slug."""
        desc = getattr(self, "entity_description", None)
        return desc.key if desc is not None else None

    def __init__(self, coordinator: SwegonModbusCoordinator) -> None:
        """Initialise the base entity."""
        super().__init__(coordinator)
        self._unavailable_logged = False

    @property
    def available(self) -> bool:
        """Return True when the coordinator last update succeeded."""
        if not super().available:
            if not self._unavailable_logged:
                _LOGGER.info(
                    "Entity %s is unavailable (coordinator update failed)",
                    self.entity_description.key
                    if self.entity_description
                    else "unknown",
                )
                self._unavailable_logged = True
            return False
        if self._unavailable_logged:
            _LOGGER.info(
                "Entity %s is back online",
                self.entity_description.key if self.entity_description else "unknown",
            )
            self._unavailable_logged = False
        return True
