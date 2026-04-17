"""Data models for the Swegon Modbus integration.

This module is intentionally kept free of platform imports so that
coordinator.py and sensor.py can both import from here without creating
an import cycle.

Import hierarchy (no cycles):
    const.py  ←  models.py  ←  coordinator.py  ←  sensor.py
                                               ←  __init__.py

Register addressing note:
    Swegon CASA Smart uses Modbus register notation 3xNNNN (input) and
    4xNNNN (holding). The 0-based pymodbus address is register_number - 1.
    Example: 3x6201 → address 6200, 4x5001 → address 5000.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.button import ButtonEntityDescription
from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntityDescription,
    NumberMode,
)
from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.components.switch import SwitchEntityDescription
from homeassistant.const import (
    CONCENTRATION_PARTS_PER_MILLION,
    EntityCategory,
    PERCENTAGE,
    UnitOfPressure,
    UnitOfTemperature,
    UnitOfTime,
)

from .const import (
    DATA_TYPE_ASCII,
    DATA_TYPE_INT16,
    DATA_TYPE_UINT16,
    INPUT_TYPE_HOLDING,
    INPUT_TYPE_INPUT,
)


@dataclass(frozen=True, kw_only=True)
class ModbusSensorEntityDescription(SensorEntityDescription):
    """Extends SensorEntityDescription with Modbus-specific register metadata."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None
    native_unit_of_measurement: str | None = None
    device_class: SensorDeviceClass | None = None
    state_class: SensorStateClass | str | None = None

    address: int = 0
    input_type: str = INPUT_TYPE_INPUT
    data_type: str = DATA_TYPE_INT16
    register_count: int = 1
    scale: float = 1.0
    precision: int = 0
    value_map: dict[int, str] | None = None
    options: list[str] | None = None


@dataclass(frozen=True, kw_only=True)
class ModbusBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Extends BinarySensorEntityDescription with Modbus-specific register metadata."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None
    device_class: BinarySensorDeviceClass | None = None

    address: int = 0
    input_type: str = INPUT_TYPE_INPUT
    data_type: str = DATA_TYPE_UINT16
    bit_position: int | None = None


@dataclass(frozen=True, kw_only=True)
class ModbusCombinedSensorEntityDescription(SensorEntityDescription):
    """A sensor whose value is derived by combining multiple Modbus register reads."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None
    native_unit_of_measurement: str | None = None
    device_class: SensorDeviceClass | None = None
    state_class: SensorStateClass | str | None = None

    components: tuple[ModbusSensorEntityDescription, ...]
    format_fn: Callable[[list[float]], str] | None = None
    value_fn: Callable[[list[float]], float] | None = None


@dataclass(frozen=True, kw_only=True)
class ModbusSwitchEntityDescription(SwitchEntityDescription):
    """Switch entity backed by a Modbus holding register (0=off, 1=on)."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None

    address: int = 0
    input_type: str = INPUT_TYPE_HOLDING
    data_type: str = DATA_TYPE_UINT16
    available_when: dict[str, float] | None = None


@dataclass(frozen=True, kw_only=True)
class ModbusSelectEntityDescription(SelectEntityDescription):
    """Select entity backed by a Modbus holding register."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None

    options: list[str] | None = None
    value_map: dict[int, str]

    address: int = 0
    input_type: str = INPUT_TYPE_HOLDING
    data_type: str = DATA_TYPE_UINT16


@dataclass(frozen=True, kw_only=True)
class ModbusNumberEntityDescription(NumberEntityDescription):
    """Number entity backed by a Modbus holding register."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None
    native_unit_of_measurement: str | None = None
    device_class: NumberDeviceClass | None = None
    mode: NumberMode = NumberMode.BOX

    address: int = 0
    input_type: str = INPUT_TYPE_HOLDING
    data_type: str = DATA_TYPE_UINT16
    scale: float = 1.0
    native_min_value: float = 0.0
    native_max_value: float = 100.0
    native_step: float = 1.0
    available_when: dict[str, float] | None = None


@dataclass(frozen=True, kw_only=True)
class ModbusButtonEntityDescription(ButtonEntityDescription):
    """Button entity that writes a fixed value to a Modbus holding register."""

    key: str
    translation_key: str | None = None
    entity_registry_enabled_default: bool = True
    entity_category: EntityCategory | None = None

    address: int = 0
    input_type: str = INPUT_TYPE_HOLDING
    data_type: str = DATA_TYPE_UINT16
    write_value: int = 1


# ---------------------------------------------------------------------------
# Helper factories
# ---------------------------------------------------------------------------


def create_temp_sensor(
    key: str,
    address: int,
    *,
    scale: float = 0.1,
    precision: int = 1,
    data_type: str = DATA_TYPE_INT16,
    entity_registry_enabled_default: bool = True,
) -> ModbusSensorEntityDescription:
    """Create a temperature sensor description with standard defaults."""
    return ModbusSensorEntityDescription(
        key=key,
        translation_key=key,
        address=address,
        data_type=data_type,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        scale=scale,
        precision=precision,
        entity_registry_enabled_default=entity_registry_enabled_default,
    )


def create_generic_sensor(
    key: str,
    address: int,
    data_type: str = DATA_TYPE_UINT16,
    native_unit_of_measurement: str | None = None,
    state_class: SensorStateClass | str | None = SensorStateClass.MEASUREMENT,
    scale: float = 1.0,
    precision: int = 0,
    device_class: SensorDeviceClass | None = None,
    options: list[str] | None = None,
    value_map: dict[int, str] | None = None,
    entity_registry_enabled_default: bool = True,
    entity_category: EntityCategory | None = None,
) -> ModbusSensorEntityDescription:
    """Create a generic sensor description with standard defaults."""
    return ModbusSensorEntityDescription(
        key=key,
        translation_key=key,
        address=address,
        data_type=data_type,
        native_unit_of_measurement=native_unit_of_measurement,
        state_class=state_class,
        scale=scale,
        precision=precision,
        device_class=device_class,
        options=options,
        value_map=value_map,
        entity_registry_enabled_default=entity_registry_enabled_default,
        entity_category=entity_category,
    )


def create_percent_number(
    key: str,
    address: int,
    *,
    min_value: float = 0,
    max_value: float = 100,
    data_type: str = DATA_TYPE_UINT16,
) -> ModbusNumberEntityDescription:
    """Create a percentage number (CONFIG)."""
    return ModbusNumberEntityDescription(
        key=key,
        translation_key=key,
        address=address,
        data_type=data_type,
        native_unit_of_measurement=PERCENTAGE,
        native_min_value=min_value,
        native_max_value=max_value,
        entity_category=EntityCategory.CONFIG,
    )


def create_temp_number(
    key: str,
    address: int,
    *,
    min_value: float,
    max_value: float,
    data_type: str = DATA_TYPE_UINT16,
    scale: float = 1.0,
) -> ModbusNumberEntityDescription:
    """Create a temperature number (CONFIG)."""
    return ModbusNumberEntityDescription(
        key=key,
        translation_key=key,
        address=address,
        data_type=data_type,
        scale=scale,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=NumberDeviceClass.TEMPERATURE,
        native_min_value=min_value,
        native_max_value=max_value,
        entity_category=EntityCategory.CONFIG,
    )


def create_duration_number(
    key: str,
    address: int,
    *,
    min_value: float = 0,
    max_value: float,
    unit: str = UnitOfTime.MINUTES,
) -> ModbusNumberEntityDescription:
    """Create a duration number (CONFIG)."""
    return ModbusNumberEntityDescription(
        key=key,
        translation_key=key,
        address=address,
        native_unit_of_measurement=unit,
        device_class=NumberDeviceClass.DURATION,
        native_min_value=min_value,
        native_max_value=max_value,
        entity_category=EntityCategory.CONFIG,
    )


# ---------------------------------------------------------------------------
# Sensor definitions — Input registers (FC4, read-only)
# ---------------------------------------------------------------------------

_UNIT_STATE_MAP: dict[int, str] = {
    0: "ext_stop",
    1: "user_stop",
    2: "starting",
    3: "normal",
    4: "commissioning",
}

_OPERATING_MODE_MAP: dict[int, str] = {
    0: "stopped",
    1: "away",
    2: "home",
    3: "boost",
    4: "travelling",
}

SENSOR_DESCRIPTIONS: tuple[ModbusSensorEntityDescription, ...] = (
    # -------------------------------------------------------------------------
    # Temperature sensors — Input registers 3x6201–3x6211
    # -------------------------------------------------------------------------
    create_temp_sensor("fresh_air_temp", 6200),  # 3x6201
    create_temp_sensor(  # 3x6202 — before re-heater
        "supply_air_before_reheater_temp",
        6201,
    ),
    create_temp_sensor("supply_air_temp", 6202),  # 3x6203
    create_temp_sensor("extract_air_temp", 6203),  # 3x6204
    create_temp_sensor("exhaust_air_temp", 6204),  # 3x6205 — exhaust (waste) air
    create_temp_sensor("room_air_temp", 6205),  # 3x6206
    create_temp_sensor(  # 3x6207
        "user_panel_1_temp",
        6206,
    ),
    create_temp_sensor(  # 3x6208
        "user_panel_2_temp",
        6207,
    ),
    create_temp_sensor(  # 3x6209 — only units with water radiator
        "water_radiator_temp",
        6208,
    ),
    create_temp_sensor(  # 3x6210 — only units with preheater
        "preheater_temp",
        6209,
    ),
    create_temp_sensor(  # 3x6211 — only if external preheater/cooling selected
        "external_fresh_air_temp",
        6210,
    ),
    # -------------------------------------------------------------------------
    # Indoor air quality — Input registers 3x6212–3x6217
    # -------------------------------------------------------------------------
    create_generic_sensor(  # 3x6212 — CO2 unfiltered
        "co2_unfiltered",
        6211,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
    ),
    create_generic_sensor(
        "co2",
        6212,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        scale=1.0,
        precision=0,
        device_class=SensorDeviceClass.CO2,
    ),  # 3x6213 — CO2 filtered
    create_generic_sensor(
        "humidity",
        6213,
        native_unit_of_measurement=PERCENTAGE,
        scale=1.0,
        precision=0,
        device_class=SensorDeviceClass.HUMIDITY,
    ),  # 3x6214
    create_generic_sensor(  # 3x6215 — absolute humidity 0.1 g/m³
        "absolute_humidity",
        6214,
        native_unit_of_measurement="g/m³",
        scale=0.1,
        precision=1,
    ),
    create_generic_sensor(  # 3x6216 — AH setpoint 0.1 g/m³
        "absolute_humidity_setpoint",
        6215,
        native_unit_of_measurement="g/m³",
        scale=0.1,
        precision=1,
    ),
    create_generic_sensor(
        "voc",
        6216,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        scale=1.0,
        precision=0,
        device_class=SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS_PARTS,
    ),  # 3x6217
    # -------------------------------------------------------------------------
    # Duct pressure and airflow — Input registers 3x6218–3x6221
    # -------------------------------------------------------------------------
    create_generic_sensor(
        "supply_duct_pressure",
        6217,
        native_unit_of_measurement=UnitOfPressure.PA,
        device_class=SensorDeviceClass.PRESSURE,
        precision=0,
    ),  # 3x6218
    create_generic_sensor(
        "exhaust_duct_pressure",
        6218,
        native_unit_of_measurement=UnitOfPressure.PA,
        device_class=SensorDeviceClass.PRESSURE,
        precision=0,
    ),  # 3x6219
    create_generic_sensor(
        "supply_air_flow",
        6219,
        native_unit_of_measurement="L/s",
        precision=0,
    ),  # 3x6220
    create_generic_sensor(
        "exhaust_air_flow",
        6220,
        native_unit_of_measurement="L/s",
        precision=0,
    ),  # 3x6221
    # -------------------------------------------------------------------------
    # Unit status — Input registers 3x6301–3x6302
    # -------------------------------------------------------------------------
    create_generic_sensor(
        "unit_state",
        6300,
        device_class=SensorDeviceClass.ENUM,
        state_class=None,
        scale=1.0,
        precision=0,
        options=list(_UNIT_STATE_MAP.values()),
        value_map=_UNIT_STATE_MAP,
    ),  # 3x6301
    create_generic_sensor(
        "operating_mode_status",
        6301,
        device_class=SensorDeviceClass.ENUM,
        state_class=None,
        scale=1.0,
        precision=0,
        options=list(_OPERATING_MODE_MAP.values()),
        value_map=_OPERATING_MODE_MAP,
    ),  # 3x6302
    # -------------------------------------------------------------------------
    # Fan control output and RPM — Input registers 3x6303–3x6306, 3x6234
    # -------------------------------------------------------------------------
    create_generic_sensor(
        "supply_fan_control",
        6302,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6303
    create_generic_sensor(
        "exhaust_fan_control",
        6303,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6304
    create_generic_sensor(
        "supply_fan_speed",
        6304,
        native_unit_of_measurement="rpm",
        scale=1.0,
        precision=0,
    ),  # 3x6305
    create_generic_sensor(
        "extract_fan_speed",
        6305,
        native_unit_of_measurement="rpm",
        scale=1.0,
        precision=0,
    ),  # 3x6306
    create_generic_sensor(
        "rotor_rpm",
        6233,
        native_unit_of_measurement="rpm",
        precision=0,
    ),  # 3x6234
    # -------------------------------------------------------------------------
    # Operational status — Input registers 3x6308, 3x6310–3x6317, 3x6320
    # -------------------------------------------------------------------------
    create_generic_sensor(
        "boost_time_left",
        6307,
        native_unit_of_measurement=UnitOfTime.MINUTES,
        device_class=SensorDeviceClass.DURATION,
        precision=0,
    ),  # 3x6308
    create_generic_sensor(  # 3x6310 — A+ (CO2-based auto) control output
        "auto_co2_control",
        6309,
        data_type=DATA_TYPE_INT16,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),
    create_generic_sensor(
        "auto_rh_control",
        6310,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6311
    create_generic_sensor(
        "auto_air_quality_control_output",
        6311,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6312
    create_generic_sensor(
        "auto_temp_boost_control",
        6312,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6313
    create_generic_sensor(
        "fan_speed_limit_control",
        6313,
        data_type=DATA_TYPE_INT16,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6314
    create_generic_sensor(
        "smart_control_output",
        6314,
        data_type=DATA_TYPE_INT16,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6315
    create_generic_sensor(
        "supply_control_power",
        6316,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6317
    create_temp_sensor(  # 3x6320 — 0.1°C
        "room_controller_supply_setpoint",
        6319,
        scale=0.1,
        precision=1,
    ),
    # -------------------------------------------------------------------------
    # Mechanical / thermal function status
    # -------------------------------------------------------------------------
    create_generic_sensor(
        "defrost_status",
        6327,
        precision=0,
        state_class=None,
    ),  # 3x6328 — 0=not active, 1–4=active
    create_generic_sensor(  # 3x6340 — 0=closed (winter), 1=open (summer)
        "heat_exchanger_bypass",
        6339,
        precision=0,
        state_class=None,
    ),
    create_generic_sensor(
        "heat_exchanger_bypass_auto",
        6347,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6348
    create_generic_sensor(
        "hours_to_service",
        6342,
        native_unit_of_measurement=UnitOfTime.HOURS,
        device_class=SensorDeviceClass.DURATION,
        precision=0,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),  # 3x6343
    create_generic_sensor(
        "preheater_output_power",
        6343,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6344
    create_generic_sensor(
        "nordic_preheater_power",
        6344,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6345
    create_generic_sensor(
        "defrost_supply_limit",
        6345,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6346
    create_generic_sensor(
        "defrost_exhaust_forcing",
        6346,
        native_unit_of_measurement=PERCENTAGE,
        precision=0,
    ),  # 3x6347
    # -------------------------------------------------------------------------
    # Device information — Input registers 3x6001–3x6003
    # -------------------------------------------------------------------------
    create_generic_sensor(
        "firmware_version_major",
        6000,
        precision=0,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),  # 3x6001
    create_generic_sensor(
        "firmware_version_minor",
        6001,
        precision=0,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),  # 3x6002
    create_generic_sensor(
        "firmware_build",
        6002,
        precision=0,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),  # 3x6003
    # -------------------------------------------------------------------------
    # Device identity — ASCII multi-register reads
    # -------------------------------------------------------------------------
    # 3x6008–3x6023: Model name (16 registers, 2 ASCII bytes packed per register)
    ModbusSensorEntityDescription(
        key="model_name",
        translation_key="model_name",
        address=6007,
        data_type=DATA_TYPE_ASCII,
        register_count=16,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    # 3x6024–3x6047: Unit serial number (24 registers, 2 ASCII bytes packed per register)
    ModbusSensorEntityDescription(
        key="serial_number",
        translation_key="serial_number",
        address=6023,
        data_type=DATA_TYPE_ASCII,
        register_count=24,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)

# ---------------------------------------------------------------------------
# Binary sensor definitions — Input registers (FC4, read-only)
# ---------------------------------------------------------------------------

BINARY_SENSOR_DESCRIPTIONS: tuple[ModbusBinarySensorEntityDescription, ...] = (
    # -------------------------------------------------------------------------
    # Summary alarm / info indicators
    # -------------------------------------------------------------------------
    # 3x6132 — simple 0/1 active alarm indicator
    ModbusBinarySensorEntityDescription(
        key="alarm_active",
        translation_key="alarm_active",
        address=6131,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    # 3x6133 — simple 0/1 unconfirmed info indicator
    ModbusBinarySensorEntityDescription(
        key="info_active",
        translation_key="info_active",
        address=6132,
    ),
    # 3x6136 — bitwise active alarms (non-zero = at least one alarm active)
    ModbusBinarySensorEntityDescription(
        key="combined_alarm",
        translation_key="combined_alarm",
        address=6135,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    # 3x6137 — bitwise unconfirmed info (non-zero = at least one info active)
    ModbusBinarySensorEntityDescription(
        key="combined_info",
        translation_key="combined_info",
        address=6136,
    ),
    # 3x6129 — service reminder info
    ModbusBinarySensorEntityDescription(
        key="service_info",
        translation_key="service_info",
        address=6128,
    ),
    # -------------------------------------------------------------------------
    # Filter
    # -------------------------------------------------------------------------
    # 3x6342 — filter guard input active
    ModbusBinarySensorEntityDescription(
        key="filter_guard_active",
        translation_key="filter_guard_active",
        address=6341,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    # -------------------------------------------------------------------------
    # Function active status — Input registers 3x6307–3x6339
    # -------------------------------------------------------------------------
    # 3x6307 — Travelling function active
    ModbusBinarySensorEntityDescription(
        key="travelling_active",
        translation_key="travelling_active",
        address=6306,
    ),
    # 3x6309 — Week timer active
    ModbusBinarySensorEntityDescription(
        key="week_timer_active",
        translation_key="week_timer_active",
        address=6308,
    ),
    # 3x6323 — Cooling control active
    ModbusBinarySensorEntityDescription(
        key="cooling_control_active",
        translation_key="cooling_control_active",
        address=6322,
    ),
    # 3x6332 — Rotor active (R-series only)
    ModbusBinarySensorEntityDescription(
        key="rotor_active",
        translation_key="rotor_active",
        address=6331,
    ),
    # 3x6333 — Preheater active
    ModbusBinarySensorEntityDescription(
        key="preheater_active",
        translation_key="preheater_active",
        address=6332,
    ),
    # 3x6334 — Summer cooling active
    ModbusBinarySensorEntityDescription(
        key="summer_cooling_active",
        translation_key="summer_cooling_active",
        address=6333,
    ),
    # 3x6335 — Fireplace function active
    ModbusBinarySensorEntityDescription(
        key="fireplace_active",
        translation_key="fireplace_active",
        address=6334,
    ),
    # 3x6336 — Central vacuum cleaner function active
    ModbusBinarySensorEntityDescription(
        key="central_vacuum_active",
        translation_key="central_vacuum_active",
        address=6335,
    ),
    # 3x6337 — Hood compensation active
    ModbusBinarySensorEntityDescription(
        key="hood_compensation_active",
        translation_key="hood_compensation_active",
        address=6336,
    ),
    # 3x6338 — External boost control active
    ModbusBinarySensorEntityDescription(
        key="external_boost_active",
        translation_key="external_boost_active",
        address=6337,
    ),
    # 3x6339 — External away control active
    ModbusBinarySensorEntityDescription(
        key="external_away_active",
        translation_key="external_away_active",
        address=6338,
    ),
    # -------------------------------------------------------------------------
    # Individual temperature sensor failures — active (3x6101–3x6108, 3x6134)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(
        key="t1_sensor_failure",
        translation_key="t1_sensor_failure",
        address=6100,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t2_sensor_failure",
        translation_key="t2_sensor_failure",
        address=6101,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t3_sensor_failure",
        translation_key="t3_sensor_failure",
        address=6102,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t4_sensor_failure",
        translation_key="t4_sensor_failure",
        address=6103,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t5_sensor_failure",
        translation_key="t5_sensor_failure",
        address=6104,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t6_sensor_failure",
        translation_key="t6_sensor_failure",
        address=6105,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t7_sensor_failure",
        translation_key="t7_sensor_failure",
        address=6106,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t8_sensor_failure",
        translation_key="t8_sensor_failure",
        address=6107,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6134
        key="t9_sensor_failure",
        translation_key="t9_sensor_failure",
        address=6133,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    # -------------------------------------------------------------------------
    # Individual temperature sensor failures — unconfirmed (3x6109–3x6116, 3x6135)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(
        key="t1_sensor_failure_unconfirmed",
        translation_key="t1_sensor_failure_unconfirmed",
        address=6108,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t2_sensor_failure_unconfirmed",
        translation_key="t2_sensor_failure_unconfirmed",
        address=6109,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t3_sensor_failure_unconfirmed",
        translation_key="t3_sensor_failure_unconfirmed",
        address=6110,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t4_sensor_failure_unconfirmed",
        translation_key="t4_sensor_failure_unconfirmed",
        address=6111,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t5_sensor_failure_unconfirmed",
        translation_key="t5_sensor_failure_unconfirmed",
        address=6112,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t6_sensor_failure_unconfirmed",
        translation_key="t6_sensor_failure_unconfirmed",
        address=6113,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t7_sensor_failure_unconfirmed",
        translation_key="t7_sensor_failure_unconfirmed",
        address=6114,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(
        key="t8_sensor_failure_unconfirmed",
        translation_key="t8_sensor_failure_unconfirmed",
        address=6115,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6135 — auto-confirmed by device
        key="t9_sensor_failure_unconfirmed",
        translation_key="t9_sensor_failure_unconfirmed",
        address=6134,
        entity_registry_enabled_default=False,
    ),
    # -------------------------------------------------------------------------
    # Heater / freezing alarms (3x6117–3x6122)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(  # 3x6117
        key="afterheater_failure",
        translation_key="afterheater_failure",
        address=6116,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6118
        key="afterheater_failure_unconfirmed",
        translation_key="afterheater_failure_unconfirmed",
        address=6117,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6119
        key="preheater_failure",
        translation_key="preheater_failure",
        address=6118,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6120
        key="preheater_failure_unconfirmed",
        translation_key="preheater_failure_unconfirmed",
        address=6119,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6121
        key="freezing_danger",
        translation_key="freezing_danger",
        address=6120,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6122
        key="freezing_danger_unconfirmed",
        translation_key="freezing_danger_unconfirmed",
        address=6121,
        entity_registry_enabled_default=False,
    ),
    # -------------------------------------------------------------------------
    # Internal temperature / fan alarms (3x6123–3x6128)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(  # 3x6123
        key="internal_temp_alarm",
        translation_key="internal_temp_alarm",
        address=6122,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6124
        key="internal_temp_alarm_unconfirmed",
        translation_key="internal_temp_alarm_unconfirmed",
        address=6123,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6125
        key="supply_fan_failure",
        translation_key="supply_fan_failure",
        address=6124,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6126
        key="supply_fan_failure_unconfirmed",
        translation_key="supply_fan_failure_unconfirmed",
        address=6125,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6127
        key="exhaust_fan_failure",
        translation_key="exhaust_fan_failure",
        address=6126,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6128
        key="exhaust_fan_failure_unconfirmed",
        translation_key="exhaust_fan_failure_unconfirmed",
        address=6127,
        entity_registry_enabled_default=False,
    ),
    # -------------------------------------------------------------------------
    # Filter / emergency stop (3x6130–3x6131)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(  # 3x6130
        key="filter_guard_unconfirmed",
        translation_key="filter_guard_unconfirmed",
        address=6129,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6131
        key="emergency_stop_active",
        translation_key="emergency_stop_active",
        address=6130,
        device_class=BinarySensorDeviceClass.PROBLEM,
    ),
    # -------------------------------------------------------------------------
    # Supply / preheater temperature alarms (3x6141–3x6146)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(  # 3x6141
        key="preheater_temp_high",
        translation_key="preheater_temp_high",
        address=6140,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6142
        key="preheater_temp_high_unconfirmed",
        translation_key="preheater_temp_high_unconfirmed",
        address=6141,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6143
        key="supply_temp_low",
        translation_key="supply_temp_low",
        address=6142,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6144
        key="supply_temp_low_unconfirmed",
        translation_key="supply_temp_low_unconfirmed",
        address=6143,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6145
        key="supply_temp_high",
        translation_key="supply_temp_high",
        address=6144,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6146
        key="supply_temp_high_unconfirmed",
        translation_key="supply_temp_high_unconfirmed",
        address=6145,
        entity_registry_enabled_default=False,
    ),
    # -------------------------------------------------------------------------
    # Rotor / fan control alarms (3x6147–3x6150, SW 3.1+ where noted)
    # -------------------------------------------------------------------------
    ModbusBinarySensorEntityDescription(  # 3x6147 — SW 3.1+
        key="rotor_alarm",
        translation_key="rotor_alarm",
        address=6146,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6148 — SW 3.1+
        key="rotor_alarm_unconfirmed",
        translation_key="rotor_alarm_unconfirmed",
        address=6147,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6149
        key="fan_control_alarm",
        translation_key="fan_control_alarm",
        address=6148,
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_registry_enabled_default=False,
    ),
    ModbusBinarySensorEntityDescription(  # 3x6150 — SW 3.1+
        key="fan_control_alarm_unconfirmed",
        translation_key="fan_control_alarm_unconfirmed",
        address=6149,
        entity_registry_enabled_default=False,
    ),
)

# ---------------------------------------------------------------------------
# Combined sensor definitions (derived from multiple registers)
# ---------------------------------------------------------------------------

COMBINED_SENSOR_DESCRIPTIONS: tuple[ModbusCombinedSensorEntityDescription, ...] = ()

# ---------------------------------------------------------------------------
# Switch definitions — Holding registers (FC3/FC6), 0=off, 1=on
# ---------------------------------------------------------------------------

SWITCH_DESCRIPTIONS: tuple[ModbusSwitchEntityDescription, ...] = (
    # 4x5004 — Travelling mode
    ModbusSwitchEntityDescription(
        key="travelling_mode",
        translation_key="travelling_mode",
        address=5003,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5005 — Cooker hood damper
    ModbusSwitchEntityDescription(
        key="cooker_hood_damper",
        translation_key="cooker_hood_damper",
        address=5004,
    ),
    # 4x5006 — Central vacuum cleaner
    ModbusSwitchEntityDescription(
        key="central_vacuum_cleaner",
        translation_key="central_vacuum_cleaner",
        address=5005,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5009 — Auto Home/Away/Boost control by CO2
    ModbusSwitchEntityDescription(
        key="auto_home_away_boost",
        translation_key="auto_home_away_boost",
        address=5008,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5012 — Heating boost control
    ModbusSwitchEntityDescription(
        key="heating_boost_control",
        translation_key="heating_boost_control",
        address=5011,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5014 — Internal post heater (re-heater)
    ModbusSwitchEntityDescription(
        key="internal_post_heater",
        translation_key="internal_post_heater",
        address=5013,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5015 — External cooling
    ModbusSwitchEntityDescription(
        key="external_cooling",
        translation_key="external_cooling",
        address=5014,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5016 — External post heater
    ModbusSwitchEntityDescription(
        key="external_post_heater",
        translation_key="external_post_heater",
        address=5015,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5017 — External liquid coil (preheating / cooling)
    ModbusSwitchEntityDescription(
        key="external_liquid_coil",
        translation_key="external_liquid_coil",
        address=5016,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5020 — Cooker Hood function enable (separate from damper open)
    ModbusSwitchEntityDescription(
        key="cooker_hood_function",
        translation_key="cooker_hood_function",
        address=5019,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5176 — External electrical preheater
    ModbusSwitchEntityDescription(
        key="external_electrical_preheater",
        translation_key="external_electrical_preheater",
        address=5175,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5177 — Open cooker hood damper during summer night cooling
    ModbusSwitchEntityDescription(
        key="summer_cooling_cooker_hood_damper",
        translation_key="summer_cooling_cooker_hood_damper",
        address=5176,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5141 — Service reminder enable
    ModbusSwitchEntityDescription(
        key="service_reminder_enable",
        translation_key="service_reminder_enable",
        address=5140,
        entity_category=EntityCategory.CONFIG,
    ),
    # -------------------------------------------------------------------------
    # Smart function visibility — User Panel display control
    # -------------------------------------------------------------------------
    # 4x5201 — Fireplace function visibility in smart functions
    ModbusSwitchEntityDescription(
        key="fireplace_smart_visibility",
        translation_key="fireplace_smart_visibility",
        address=5200,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5202 — Travelling mode visibility in smart functions
    ModbusSwitchEntityDescription(
        key="travelling_smart_visibility",
        translation_key="travelling_smart_visibility",
        address=5201,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5204 — Central vacuum function visibility in smart functions
    ModbusSwitchEntityDescription(
        key="central_vacuum_smart_visibility",
        translation_key="central_vacuum_smart_visibility",
        address=5203,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5205 — Summer night cooling visibility in smart functions
    ModbusSwitchEntityDescription(
        key="summer_cooling_smart_visibility",
        translation_key="summer_cooling_smart_visibility",
        address=5204,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5206 — Heating boost visibility in smart functions
    ModbusSwitchEntityDescription(
        key="heating_boost_smart_visibility",
        translation_key="heating_boost_smart_visibility",
        address=5205,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5207 — Shutdown visibility in smart functions (units with User Panel only)
    ModbusSwitchEntityDescription(
        key="shutdown_smart_visibility",
        translation_key="shutdown_smart_visibility",
        address=5206,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5208 — Auto humidity control visibility in smart functions (SW 3.1+)
    ModbusSwitchEntityDescription(
        key="auto_humidity_smart_visibility",
        translation_key="auto_humidity_smart_visibility",
        address=5207,
        entity_category=EntityCategory.CONFIG,
    ),
)

# ---------------------------------------------------------------------------
# Select definitions — Holding registers (FC3/FC6), enumerated options
# ---------------------------------------------------------------------------

SELECT_DESCRIPTIONS: tuple[ModbusSelectEntityDescription, ...] = (
    # 4x5001 — Operating mode (main control)
    ModbusSelectEntityDescription(
        key="operating_mode",
        translation_key="operating_mode",
        address=5000,
        options=["stopped", "away", "home", "boost", "travelling"],
        value_map={0: "stopped", 1: "away", 2: "home", 3: "boost", 4: "travelling"},
    ),
    # 4x5018 — Emergency stop
    ModbusSelectEntityDescription(
        key="emergency_stop",
        translation_key="emergency_stop",
        address=5017,
        entity_category=EntityCategory.CONFIG,
        options=["disabled", "active", "overpressurizing"],
        value_map={0: "disabled", 1: "active", 2: "overpressurizing"},
    ),
    # 4x5010 — Auto humidity control (SW 3.1+)
    ModbusSelectEntityDescription(
        key="auto_humidity_control",
        translation_key="auto_humidity_control",
        address=5009,
        entity_category=EntityCategory.CONFIG,
        options=["off", "user", "low", "normal", "high", "full"],
        value_map={0: "off", 1: "user", 2: "low", 3: "normal", 4: "high", 5: "full"},
    ),
    # 4x5011 — Auto air quality (VOC) control (SW 3.1+)
    ModbusSelectEntityDescription(
        key="auto_air_quality_control",
        translation_key="auto_air_quality_control",
        address=5010,
        entity_category=EntityCategory.CONFIG,
        options=["off", "user", "low", "normal", "high", "full"],
        value_map={0: "off", 1: "user", 2: "low", 3: "normal", 4: "high", 5: "full"},
    ),
    # 4x5130 — Temperature controller method
    ModbusSelectEntityDescription(
        key="temperature_controller_method",
        translation_key="temperature_controller_method",
        address=5129,
        entity_category=EntityCategory.CONFIG,
        options=["supply_air", "room_air"],
        value_map={0: "supply_air", 1: "room_air"},
    ),
    # 4x5164 — Summer night cooling control
    ModbusSelectEntityDescription(
        key="summer_night_cooling_control",
        translation_key="summer_night_cooling_control",
        address=5163,
        entity_category=EntityCategory.CONFIG,
        options=["off", "low", "normal", "high", "full", "user"],
        value_map={0: "off", 1: "low", 2: "normal", 3: "high", 4: "full", 5: "user"},
    ),
    # 4x5174 — Heating mode
    ModbusSelectEntityDescription(
        key="heating_mode",
        translation_key="heating_mode",
        address=5173,
        entity_category=EntityCategory.CONFIG,
        options=["not_available", "eco", "comfort"],
        value_map={0: "not_available", 1: "eco", 2: "comfort"},
    ),
    # 4x5152 — Room temperature sensor source
    ModbusSelectEntityDescription(
        key="room_temperature_sensor",
        translation_key="room_temperature_sensor",
        address=5151,
        entity_category=EntityCategory.CONFIG,
        options=["internal", "t6", "t7", "t8", "t9", "up1", "up2"],
        value_map={
            0: "internal",
            1: "t6",
            2: "t7",
            3: "t8",
            4: "t9",
            5: "up1",
            6: "up2",
        },
    ),
    # 4x5153 — Supply temperature sensor source
    ModbusSelectEntityDescription(
        key="supply_temperature_sensor",
        translation_key="supply_temperature_sensor",
        address=5152,
        entity_category=EntityCategory.CONFIG,
        options=["internal", "t6", "t7", "t8", "t9"],
        value_map={0: "internal", 1: "t6", 2: "t7", 3: "t8", 4: "t9"},
    ),
    # 4x5154 — Outside temperature sensor source
    ModbusSelectEntityDescription(
        key="outside_temperature_sensor",
        translation_key="outside_temperature_sensor",
        address=5153,
        entity_category=EntityCategory.CONFIG,
        options=["internal", "t6", "t7", "t8", "t9"],
        value_map={0: "internal", 1: "t6", 2: "t7", 3: "t8", 4: "t9"},
    ),
    # 4x5156 — Water temperature sensor source
    ModbusSelectEntityDescription(
        key="water_temperature_sensor",
        translation_key="water_temperature_sensor",
        address=5155,
        entity_category=EntityCategory.CONFIG,
        options=["internal", "t6", "t7", "t8", "t9"],
        value_map={0: "internal", 1: "t6", 2: "t7", 3: "t8", 4: "t9"},
    ),
    # 4x5169 — Summer night cooling boost control mode
    ModbusSelectEntityDescription(
        key="summer_night_cooling_boost_control",
        translation_key="summer_night_cooling_boost_control",
        address=5168,
        entity_category=EntityCategory.CONFIG,
        options=["off", "low", "normal", "high", "full", "user"],
        value_map={0: "off", 1: "low", 2: "normal", 3: "high", 4: "full", 5: "user"},
    ),
)

# ---------------------------------------------------------------------------
# Number definitions — Holding registers (FC3/FC6), writable ranges
# ---------------------------------------------------------------------------

NUMBER_DESCRIPTIONS: tuple[ModbusNumberEntityDescription, ...] = (
    # -------------------------------------------------------------------------
    # Primary setpoints
    # -------------------------------------------------------------------------
    # 4x5101 — Temperature setpoint (13–25 °C)
    create_temp_number(
        "temperature_setpoint",
        5100,
        min_value=13,
        max_value=25,
        data_type="int16",
    ),
    # 4x5019 — Smart control (-100..100 %)
    ModbusNumberEntityDescription(
        key="smart_control",
        translation_key="smart_control",
        address=5018,
        data_type="int16",
        native_unit_of_measurement=PERCENTAGE,
        native_min_value=-100,
        native_max_value=100,
    ),
    # -------------------------------------------------------------------------
    # Fan speed percentages (away / home / boost)
    # -------------------------------------------------------------------------
    create_percent_number("supply_fan_speed_away", 5301, min_value=20),
    create_percent_number("exhaust_fan_speed_away", 5302, min_value=20),
    create_percent_number("supply_fan_speed_home", 5303, min_value=20),
    create_percent_number("exhaust_fan_speed_home", 5304, min_value=20),
    create_percent_number("supply_fan_speed_boost", 5305, min_value=20),
    create_percent_number("exhaust_fan_speed_boost", 5306, min_value=20),
    # 4x5308 — Max smart boost limitation (% of Boost)
    create_percent_number("max_smart_boost", 5307),
    # -------------------------------------------------------------------------
    # Fireplace function settings
    # -------------------------------------------------------------------------
    create_duration_number("fireplace_run_time", 5103, max_value=60),
    create_percent_number("fireplace_max_speed_diff", 5104, max_value=25),
    # -------------------------------------------------------------------------
    # Travelling mode settings
    # -------------------------------------------------------------------------
    create_percent_number("travelling_speed_drop", 5105, max_value=20),
    create_temp_number("travelling_temp_drop", 5106, min_value=0, max_value=10),
    # -------------------------------------------------------------------------
    # Away state temperature
    # -------------------------------------------------------------------------
    create_temp_number("away_temp_drop", 5170, min_value=0, max_value=10),
    # -------------------------------------------------------------------------
    # CO2-based auto control limits
    # -------------------------------------------------------------------------
    ModbusNumberEntityDescription(
        key="co2_home_limit",
        translation_key="co2_home_limit",
        address=5113,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=NumberDeviceClass.CO2,
        native_min_value=0,
        native_max_value=2000,
        entity_category=EntityCategory.CONFIG,
    ),
    ModbusNumberEntityDescription(
        key="co2_away_limit",
        translation_key="co2_away_limit",
        address=5114,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=NumberDeviceClass.CO2,
        native_min_value=0,
        native_max_value=2000,
        entity_category=EntityCategory.CONFIG,
    ),
    # -------------------------------------------------------------------------
    # RH auto control limits
    # -------------------------------------------------------------------------
    create_percent_number("rh_boost_limit", 5116, max_value=50),
    create_percent_number("rh_full_boost_limit", 5117, max_value=50),
    # -------------------------------------------------------------------------
    # VOC auto control limits
    # -------------------------------------------------------------------------
    ModbusNumberEntityDescription(
        key="voc_boost_limit",
        translation_key="voc_boost_limit",
        address=5120,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        native_min_value=0,
        native_max_value=2000,
        entity_category=EntityCategory.CONFIG,
    ),
    ModbusNumberEntityDescription(
        key="voc_full_boost_limit",
        translation_key="voc_full_boost_limit",
        address=5121,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        native_min_value=0,
        native_max_value=2000,
        entity_category=EntityCategory.CONFIG,
    ),
    # -------------------------------------------------------------------------
    # Summer night cooling
    # -------------------------------------------------------------------------
    create_temp_number(
        "summer_cooling_fresh_air_limit", 5164, min_value=0, max_value=25
    ),
    create_temp_number(
        "summer_cooling_room_temp_limit", 5166, min_value=0, max_value=35
    ),
    create_temp_number(
        "summer_cooling_min_supply_temp", 5167, min_value=10, max_value=25
    ),
    create_temp_number(
        "summer_cooling_boost_room_limit", 5169, min_value=18, max_value=28
    ),  # 4x5170
    create_temp_number(  # 4x5125 — SW 3.1+
        "summer_cooling_full_boost_room_limit", 5124, min_value=18, max_value=40
    ),
    create_temp_number(  # 4x5166 — fresh air start limit for summer cooling
        "summer_cooling_fresh_air_start_limit", 5165, min_value=0, max_value=25
    ),
    # -------------------------------------------------------------------------
    # Cooker hood
    # -------------------------------------------------------------------------
    create_percent_number(
        "cooker_hood_home_compensation", 5108, max_value=50
    ),  # 4x5109
    create_percent_number(
        "cooker_hood_boost_compensation", 5109, max_value=50
    ),  # 4x5110
    create_percent_number("cooker_hood_boost_speed", 5150),  # 4x5151
    # -------------------------------------------------------------------------
    # Central vacuum cleaner
    # -------------------------------------------------------------------------
    create_duration_number("central_vacuum_run_time", 5111, max_value=60),  # 4x5112
    create_percent_number("central_vacuum_compensation", 5112, max_value=50),  # 4x5113
    # -------------------------------------------------------------------------
    # Auto RH control timing
    # -------------------------------------------------------------------------
    create_duration_number("rh_boost_delay", 5118, max_value=30),  # 4x5119 SW 3.1+
    create_percent_number(
        "rh_boost_during_delay", 5119, max_value=25
    ),  # 4x5120 SW 3.1+
    # -------------------------------------------------------------------------
    # Heating boost
    # -------------------------------------------------------------------------
    create_percent_number("heating_boost_gain", 5123),  # 4x5124
    # -------------------------------------------------------------------------
    # Heating / cooling temperature control
    # -------------------------------------------------------------------------
    create_temp_number(  # 4x5129 — fresh air limit for heating (can be negative)
        "heating_fresh_air_limit",
        5128,
        min_value=-50,
        max_value=50,
        data_type=DATA_TYPE_INT16,
    ),
    ModbusNumberEntityDescription(  # 4x5132 — room temp fine tuning, 0.1°C steps
        key="room_temp_fine_tuning",
        translation_key="room_temp_fine_tuning",
        address=5131,
        data_type=DATA_TYPE_INT16,
        scale=0.1,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=NumberDeviceClass.TEMPERATURE,
        native_min_value=-5.0,
        native_max_value=5.0,
        native_step=0.1,
        entity_category=EntityCategory.CONFIG,
    ),
    create_temp_number(
        "room_control_supply_min", 5132, min_value=10, max_value=50
    ),  # 4x5133
    create_temp_number(
        "room_control_supply_max", 5133, min_value=10, max_value=50
    ),  # 4x5134
    create_temp_number(
        "cooling_fresh_air_limit", 5134, min_value=0, max_value=50
    ),  # 4x5135
    create_temp_number(
        "room_control_cooling_min", 5135, min_value=10, max_value=50
    ),  # 4x5136
    create_temp_number(
        "room_control_cooling_max", 5136, min_value=10, max_value=50
    ),  # 4x5137
    create_temp_number(  # 4x5138
        "external_preheating_fresh_air_limit",
        5137,
        min_value=-50,
        max_value=50,
        data_type=DATA_TYPE_INT16,
    ),
    create_temp_number(  # 4x5139
        "external_precooling_fresh_air_limit",
        5138,
        min_value=-50,
        max_value=50,
        data_type=DATA_TYPE_INT16,
    ),
    ModbusNumberEntityDescription(  # 4x5142 — service reminder interval in months
        key="service_reminder_interval",
        translation_key="service_reminder_interval",
        address=5141,
        native_unit_of_measurement="months",
        native_min_value=1,
        native_max_value=60,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
    ),
    ModbusNumberEntityDescription(  # 4x5155 — supply temp fine tuning, 0.1°C steps
        key="supply_temp_fine_tuning",
        translation_key="supply_temp_fine_tuning",
        address=5154,
        data_type=DATA_TYPE_INT16,
        scale=0.1,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=NumberDeviceClass.TEMPERATURE,
        native_min_value=-5.0,
        native_max_value=5.0,
        native_step=0.1,
        entity_category=EntityCategory.CONFIG,
    ),
)

# ---------------------------------------------------------------------------
# Button definitions — Holding registers (FC6), one-shot writes
# ---------------------------------------------------------------------------

BUTTON_DESCRIPTIONS: tuple[ModbusButtonEntityDescription, ...] = (
    # 4x5406 — Reset all info alarms
    ModbusButtonEntityDescription(
        key="reset_all_alarms",
        translation_key="reset_all_alarms",
        address=5405,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5401 — Re-heater failure alarm confirm
    ModbusButtonEntityDescription(
        key="confirm_reheater_alarm",
        translation_key="confirm_reheater_alarm",
        address=5400,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5402 — Preheater failure alarm confirm
    ModbusButtonEntityDescription(
        key="confirm_preheater_alarm",
        translation_key="confirm_preheater_alarm",
        address=5401,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5403 — Water radiator freezing danger alarm confirm
    ModbusButtonEntityDescription(
        key="confirm_freezing_alarm",
        translation_key="confirm_freezing_alarm",
        address=5402,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5404 — Filter guard info confirm
    ModbusButtonEntityDescription(
        key="confirm_filter_alarm",
        translation_key="confirm_filter_alarm",
        address=5403,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5405 — Service timer info confirm
    ModbusButtonEntityDescription(
        key="confirm_service_alarm",
        translation_key="confirm_service_alarm",
        address=5404,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5407 — Fan failure alarm confirm
    ModbusButtonEntityDescription(
        key="confirm_fan_alarm",
        translation_key="confirm_fan_alarm",
        address=5406,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5408 — Sensor failure confirm
    ModbusButtonEntityDescription(
        key="confirm_sensor_alarm",
        translation_key="confirm_sensor_alarm",
        address=5407,
        write_value=1,
        entity_category=EntityCategory.CONFIG,
    ),
    # 4x5002 — Activate fireplace function (write 1 to start)
    ModbusButtonEntityDescription(
        key="activate_fireplace",
        translation_key="activate_fireplace",
        address=5001,
        write_value=1,
    ),
)
