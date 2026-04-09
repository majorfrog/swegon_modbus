# Swegon Modbus — Home Assistant Custom Integration

A Home Assistant custom integration for controlling and monitoring **Swegon CASA** ventilation units (heat-recovery ventilators) via **Modbus RTU (RS-485)**.

The integration is built on top of [pymodbus](https://github.com/pymodbus-dev/pymodbus) using its fully async client, so it never blocks the Home Assistant event loop.

---

> **Disclaimer:** This integration is an independent community project. It is **not** owned, developed, or endorsed by Swegon Group AB or any affiliated entity. Use it entirely at your own risk. The authors accept no responsibility for damage, data loss, or any other consequence arising from its use.

---

## Use Cases

- **Monitor air quality** — track CO₂, humidity, VOC, and temperature in real time.
- **Automate ventilation** — adjust operating mode (Away / Home / Boost) based on occupancy, time of day, CO₂ level, or other automations.
- **Energy-aware control** — lower fan speeds when away and boost them when needed.
- **Maintenance alerts** — get notified when a filter change or service is due.
- **Climate integration** — use supply/room temperature readings as inputs to HA climate automations.

---

## Features

- Communicates over **Modbus RTU** (RS-485 serial)
- Configurable via the **UI** (Settings → Integrations) or directly in **`configuration.yaml`**
- Polling interval: **10 seconds** (adjusts automatically with exponential back-off on repeated failures)
- Clean disconnect on integration unload/reload
- Reconfiguration flow — update connection parameters without removing the integration

### Entities

| Platform | Count | Examples |
|---|---|---|
| **Sensor** | ~48 | Temperatures, CO₂, humidity, VOC, fan speeds, duct pressure, airflow, unit state |
| **Binary sensor** | 17 | Alarm active, filter guard, fireplace active, rotor active, function active status |
| **Switch** | 12 | Travelling mode, cooker hood damper, central vacuum, auto home/away/boost, post heater |
| **Select** | 12 | Operating mode, auto humidity/air-quality control, heating mode, temperature sensor source |
| **Number** | ~44 | Temperature setpoint, fan speed per mode (away/home/boost), CO₂/RH/VOC limits, summer cooling limits |
| **Button** | 9 | Activate fireplace, reset alarms, confirm individual alarms |

---

## Requirements

| Requirement | Value |
|---|---|
| Home Assistant | 2024.1.0 or newer |
| HACS | for easy installation (optional) |
| Python dependency | `pymodbus>=3.11,<4` (auto-installed) |

### Hardware

To use this integration with **Modbus RTU** you need something that converts RS-485 to a serial/USB interface, such as a USB-to-RS485 adapter.

On the Swegon CASA unit, the RJ45 port intended for SEC/SEM accessories is used for Modbus. If the cable is wired to the 568B standard, the RS-485 connections are:

| Wire colour  | RS-485 signal |
|--------------|---------------|
| Orange/White | A (+)         |
| Orange       | B (−)         |

---

## Installation

### HACS (recommended)

1. Open **HACS** → **Integrations** → three-dot menu → **Custom repositories**.
2. Add `https://github.com/majorfrog/swegon_modbus` with category **Integration**.
3. Search for **Swegon Modbus** and click **Download**.
4. Restart Home Assistant.

### Manual

1. Copy the `custom_components/swegon_modbus` directory into your HA `config/custom_components/` folder.
2. Restart Home Assistant.

---

## Configuration

You can set up the integration either through the UI or via `configuration.yaml`. Both methods produce the same config entry.

### Option A — UI (recommended)

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Swegon Modbus**.
3. Enter the serial port path and serial parameters.
4. The integration tests the connection before saving. If the test fails, correct the settings and try again.

### Option B — `configuration.yaml`

Add the following to your `configuration.yaml`. If you have multiple devices, use a YAML list.

```yaml
swegon_modbus:
  port: /dev/ttyUSB0      # serial device path (Linux) or COM3 (Windows)
  unit_id: 1              # optional — default: 1
  baudrate: 38400         # optional — default: 38400 (Swegon CASA default)
  bytesize: 8             # optional — default: 8  (5/6/7/8)
  parity: "N"             # optional — default: N  (N=none, E=even, O=odd)
  stopbits: 1             # optional — default: 1  (1 or 2)
```

#### Multiple devices

```yaml
swegon_modbus:
  - port: /dev/ttyUSB0
    unit_id: 1
  - port: /dev/ttyUSB1
    unit_id: 2
    baudrate: 38400
```

> **Note:** When using `configuration.yaml`, Home Assistant creates a config entry automatically on startup. No connection test is performed at import time — the device may be temporarily offline without preventing startup. You can manage or remove the entry later under **Settings → Devices & Services**.

### Configuration parameters

| Parameter | Required | Default | Description |
|---|---|---|---|
| `port` | **Yes** | — | Serial device path, e.g. `/dev/ttyUSB0` or `COM3` |
| `unit_id` | No | `1` | Modbus unit ID, 1–247 |
| `baudrate` | No | `38400` | Communication speed in bps (Swegon CASA default) |
| `bytesize` | No | `8` | Number of data bits (5, 6, 7, or 8) |
| `parity` | No | `N` | Parity: `N` (none), `E` (even), `O` (odd) — Swegon CASA uses `N` |
| `stopbits` | No | `1` | Number of stop bits (1 or 2) |

---

## Supported Devices

- **Swegon CASA** — all models that expose Modbus registers via the RJ45 service port (CASA R3, R4, R5, W3, W5, and similar).

The integration uses the documented Swegon CASA Modbus register map (input registers 3x6001–3x6348, holding registers 4x5001–4x5408). Register availability may vary between firmware versions and hardware generations.

---

## Data Updates

The integration polls the device every **10 seconds**. If the device becomes unreachable, the polling back-off increases exponentially (up to a maximum interval) to avoid flooding the bus. All entities will show as **unavailable** while the device is offline, and one log message is emitted. When connectivity is restored, entities return to normal and another log message is emitted.

---

## Dashboard

A ready-made Home Assistant dashboard is included in the repository as [`swegon.yaml`](swegon.yaml). It covers three views:

| View | Contents |
|---|---|
| **Overview** | Unit state, alarms, temperatures, air quality, airflow, fan/rotor speeds, active functions, heat exchanger |
| **Controls** | Operating mode, temperature setpoints, per-mode fan speeds, auto quality control, travelling/away, summer night cooling, special functions, room temperature control, external accessories |
| **Diagnostics** | Service & maintenance status, alarm overview, alarm confirmation, mechanical status, control outputs, all temperature sensors, firmware & device info |

### How to use it

1. In Home Assistant, go to **Settings → Dashboards** and click **Add dashboard**.
2. Give it a name (e.g. *Swegon CASA*) and confirm.
3. Open the new dashboard, click the three-dot menu (⋮) in the top-right corner and select **Edit dashboard**.
4. Click the three-dot menu again and choose **Raw configuration editor**.
5. Replace all existing content with the contents of [`swegon.yaml`](swegon.yaml) from this repository.
6. Click **Save** and then **Done**.

> **Note:** Entity IDs in the dashboard follow the pattern `{platform}.swegon_casa_{key}`. If your device was renamed during setup, replace `swegon_casa` with the lower-case, underscore-separated version of your device name throughout the file.

---

## Removal

1. Go to **Settings → Devices & Services**.
2. Find the **Swegon Modbus** integration entry.
3. Click the three-dot menu and select **Delete**.
4. If you configured it via `configuration.yaml`, also remove the `swegon_modbus:` block and restart Home Assistant.

---

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---|---|---|
| Integration shows as unavailable | Device offline or wrong serial port | Check cable and port path |
| "Failed to connect" when adding via UI | Wrong device path or serial parameters | Correct the settings and retry |
| RTU serial port not found | Wrong device path | Check `ls /dev/tty*` on Linux; ensure HA has permission to access the port |
| All sensors show `Unknown` after setup | Device connected but wrong unit ID | Verify the unit ID in the Swegon service menu |
| Values unchanged for a long time | Polling back-off after repeated failures | Check HA logs for connection errors; verify device is reachable |
| Entities missing after update | Entity registry may be stale | Reload the integration under **Settings → Devices & Services** |

---

## License

[MIT](LICENSE)
