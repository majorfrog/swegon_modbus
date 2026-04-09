"""Constants for the Swegon Modbus integration."""

from __future__ import annotations

from typing import Final

DOMAIN: Final = "swegon_modbus"

# Device identity constants
MANUFACTURER: Final = "Swegon"
MODEL: Final = "Swegon CASA"

# Shared configuration keys
CONF_UNIT_ID: Final = "unit_id"

# RTU-specific configuration keys
CONF_BAUDRATE: Final = "baudrate"
CONF_BYTESIZE: Final = "bytesize"
CONF_PARITY: Final = "parity"
CONF_STOPBITS: Final = "stopbits"

# RTU / shared defaults
DEFAULT_UNIT_ID: Final = 1
DEFAULT_BAUDRATE: Final = 38400
DEFAULT_BYTESIZE: Final = 8
DEFAULT_PARITY: Final = "N"
DEFAULT_STOPBITS: Final = 1

# How often the coordinator polls the device (seconds).
SCAN_INTERVAL_SECONDS: Final = 10

# --- Register / data-type Constants ---

# input_type values (which Modbus FC to use for reading)
INPUT_TYPE_INPUT: Final = "input"  # FC 4 — read input registers
INPUT_TYPE_HOLDING: Final = "holding"  # FC 3 — read holding registers

# data_type values
DATA_TYPE_INT16: Final = "int16"
DATA_TYPE_UINT16: Final = "uint16"
DATA_TYPE_INT32: Final = "int32"
DATA_TYPE_UINT32: Final = "uint32"
DATA_TYPE_FLOAT32: Final = "float32"
DATA_TYPE_ASCII: Final = "ascii"
