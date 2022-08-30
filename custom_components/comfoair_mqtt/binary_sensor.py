"""Binary sensor platform for integration_blueprint."""
from homeassistant.components.binary_sensor import BinarySensorEntity

from .const import (
    BINARY_SENSOR_DESCRIPTIONS,
    DOMAIN,
)
from .entity import ComfoairMqttEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        ComfoairMqttBinarySensor(data, entry, description)
        for description in BINARY_SENSOR_DESCRIPTIONS
    )


class ComfoairMqttBinarySensor(ComfoairMqttEntity, BinarySensorEntity):
    """ComfoairMqtt binary_sensor class."""

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.data.get(self.entity_description.key)
