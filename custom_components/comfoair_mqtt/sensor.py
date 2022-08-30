"""Sensor platform for integration_blueprint."""
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.issue_registry import (
    IssueSeverity,
    async_create_issue,
    async_delete_issue,
)

from .const import DOMAIN, SENSOR_DESCRIPTIONS
from .entity import ComfoairMqttEntity


FILTER_ISSUE = "replace_filters"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    """Setup sensor platform."""
    data = hass.data[DOMAIN][entry.entry_id]

    entries = [
        ComfoairMqttSensor(data, entry, description)
        for description in SENSOR_DESCRIPTIONS
    ]
    entries.append(ComfoairMqttFilterSensor(data, entry, hass))
    async_add_devices(entries)


class ComfoairMqttSensor(ComfoairMqttEntity, SensorEntity):
    """ComfoairMqtt Sensor class."""

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self.data.get(self.entity_description.key)


class ComfoairMqttFilterSensor(ComfoairMqttEntity, SensorEntity):
    """ComfoairMqtt Sensor class."""

    def __init__(self, data, config_entry: ConfigEntry, hass: HomeAssistant):
        super().__init__(
            data,
            config_entry,
            SensorEntityDescription(
                key="filter_error_intern",
                name="Filter intern",
            ),
        )
        self.hass = hass

    def check_if_filter_change_needed(self, value) -> None:
        """Checks if a filter change is needed and creates an issue."""
        if value and int(value) == 0:
            async_create_issue(
                self.hass,
                DOMAIN,
                FILTER_ISSUE,
                is_fixable=False,
                severity=IssueSeverity.WARNING,
                translation_key="replace_filters",
                learn_more_url="https://www.home-assistant.io/",
            )
        else:
            async_delete_issue(self.hass, DOMAIN, FILTER_ISSUE)

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        value = self.data.get(self.entity_description.key)
        self.check_if_filter_change_needed(value)
        return value
