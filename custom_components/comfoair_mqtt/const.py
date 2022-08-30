"""Constants for comfoair-mqtt integration."""

from statistics import mode
from homeassistant.const import Platform, TEMP_CELSIUS, TIME_HOURS, PERCENTAGE

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.components.binary_sensor import BinarySensorEntityDescription
from homeassistant.components.number import NumberEntityDescription

# Base component constants
NAME = "Comfoair MQTT"
DOMAIN = "comfoair_mqtt"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/pail23/comfoair-mqtt-integration/issues"

MANUFACTURER = "Zehnder"
MODEL = "Comfoair 550"

TOPIC = "comfoair/"
SUBSCRIBE_TOPIC = TOPIC + "#"

# Icons
ICON = "mdi:format-quote-close"

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR, Platform.NUMBER]


# Configuration and options
CONF_ENABLED = "enabled"


# Defaults
DEFAULT_NAME = DOMAIN


SENSOR_DESCRIPTIONS = (
    SensorEntityDescription(
        key="outdoor_incomming_temperature",
        name="Outdoor incomming temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="outdoor_outgoing_temperature",
        name="Outdoor outgoing temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="indoor_incomming_temperature",
        name="Indoor incomming temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="indoor_outgoing_temperature",
        name="Indoor outgoing temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="comfort_temperature",
        name="Target temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="incomming_fan",
        name="Incomming fan",
        icon="mdi:fan",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="outgoing_fan",
        name="Outgoing fan",
        icon="mdi:fan",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="filter_hours",
        name="Filter hours",
        icon="hass:clock",
        native_unit_of_measurement=TIME_HOURS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="successfull_sent_commands",
        name="Successfull commands",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="failed_sent_commands",
        name="Failed commands",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="error_message",
        name="Error code",
    ),
    SensorEntityDescription(
        key="filter_error_extern",
        name="Filter extern",
    ),
)

BINARY_SENSOR_DESCRIPTIONS = (
    BinarySensorEntityDescription(key="bypass_mode", name="Bypass mode"),
    BinarySensorEntityDescription(key="bypass_summer_mode", name="Bypass summer mode"),
    BinarySensorEntityDescription(key="filter_status", name="Filter status"),
)

NUMBER_DESCRIPTIONS = [
    NumberEntityDescription(
        key="fan_level",
        name="Fan Level",
        min_value=1,
        max_value=4,
        native_step=1,
        step=1,
    )
]


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
