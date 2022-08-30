"""Sensor platform for Comfoair MQTT."""
from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components import mqtt

from .const import DOMAIN, NUMBER_DESCRIPTIONS, TOPIC
from .entity import ComfoairMqttEntity


FILTER_ISSUE = "replace_filters"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    """Setup number platform."""
    data = hass.data[DOMAIN][entry.entry_id]

    async_add_devices(
        ComfoairMqttNumber(data, entry, description)
        for description in NUMBER_DESCRIPTIONS
    )


class ComfoairMqttNumber(ComfoairMqttEntity, NumberEntity):
    """ComfoairMqtt number class."""

    @property
    def native_value(self) -> float | None:
        """Return the native value of the sensor."""
        value = self.data.get(self.entity_description.key)
        if value is None:
            return None
        return float(value)

    async def async_set_native_value(self, value: float) -> None:
        """Set new value."""
        message = f"{int(value)}"
        topic = f"{TOPIC}{self.entity_description.key}/set"
        await mqtt.async_publish(self.hass, topic, message)
        self.data[self.entity_description.key] = message
