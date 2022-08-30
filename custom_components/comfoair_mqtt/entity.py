"""ComfoairMqttEntity class"""

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity import Entity, DeviceInfo, EntityDescription
from .const import DOMAIN, NAME, MODEL, MANUFACTURER


class ComfoairMqttEntity(Entity):
    """Comfoair Mqtt entity."""

    _attr_has_entity_name = True

    def __init__(self, data, config_entry: ConfigEntry, description: EntityDescription):
        self.config_entry = config_entry
        self.entity_description = description
        self.data = data

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id + "_" + self.entity_description.key

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.config_entry.entry_id)},
            name=NAME,
            model=MODEL,
            manufacturer=MANUFACTURER,
        )
