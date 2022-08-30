"""Binary sensor platform for Comfoair MQTT."""
from homeassistant.components.climate import (
    ClimateEntity,
    HVACMode,
    ClimateEntityFeature,
)
from homeassistant.components import mqtt

from homeassistant.const import TEMP_CELSIUS

from .const import (
    CLIMATE_DESCRIPTIONS,
    DOMAIN,
    INDOOR_OUTGOING_TEMPERATURE,
    TARGET_TEMPERATURE,
    FAN_MODE,
    HVAC_MODE,
    TOPIC,
)
from .entity import ComfoairMqttEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        ComfoairMqttBinarySensor(data, entry, description)
        for description in CLIMATE_DESCRIPTIONS
    )


class ComfoairMqttBinarySensor(ComfoairMqttEntity, ClimateEntity):
    """ComfoairMqtt climate class."""

    _attr_min_temp = 15
    _attr_max_temp = 27
    _attr_target_temperature_step = 1
    _attr_fan_modes = ["off", "low", "medium", "high"]
    _attr_hvac_modes = [HVACMode.OFF, HVACMode.FAN_ONLY]
    _attr_temperature_unit = TEMP_CELSIUS
    _attr_supported_features = (
        ClimateEntityFeature.FAN_MODE | ClimateEntityFeature.TARGET_TEMPERATURE
    )

    @property
    def current_temperature(self) -> float | None:
        """Return the current temperature."""
        temp = self.data.get(INDOOR_OUTGOING_TEMPERATURE)
        if temp is None:
            return None
        return float(temp)

    @property
    def target_temperature(self) -> float | None:
        """Return the temperature we try to reach."""
        temp = self.data.get(TARGET_TEMPERATURE)
        if temp is None:
            return None
        return float(temp)

    @property
    def fan_mode(self) -> str | None:
        """Return the current fan mode."""
        return self.data.get(FAN_MODE)

    @property
    def hvac_mode(self) -> HVACMode | str | None:
        """Return the current hvac mode."""
        return self.data.get(HVAC_MODE)

    async def async_set_temperature(self, **kwargs) -> None:
        message = kwargs["temperature"]
        topic = f"{TOPIC}{self.entity_description.key}/set"
        await mqtt.async_publish(self.hass, topic, message)
        self.data[self.entity_description.key] = message

    async def async_set_fan_mode(self, fan_mode: str) -> None:
        topic = f"{TOPIC}{FAN_MODE}/set"
        await mqtt.async_publish(self.hass, topic, fan_mode)
        self.data[FAN_MODE] = fan_mode

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        message = str(hvac_mode)
        topic = f"{TOPIC}{HVAC_MODE}/set"
        await mqtt.async_publish(self.hass, topic, message)
        self.data[HVAC_MODE] = hvac_mode
