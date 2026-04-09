# Swegon CASA Smart Modbus Register — SCB 3.0

> **Note:** This register list is only valid for SEM / SEC with Device version 3.0→

## USER SETTINGS

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 4x5001 | RW | Operating Mode | 0 | 4 | | 0=Stopped, 1=Away, 2=Home, 3=Boost, 4=Travelling | |
| 3.0→ | 4x5019 | RW | Smart Control | -100 | 100 | % | Smart control — increase or decrease ventilation level steplessly based on Home level. When value is 0 the Smart function is disabled. | |
| 3.0→ | 4x5018 | RW | Emergency Stop | 0 | 2 | | 0=Emergency stop disabled, 1=Emergency stop enabled, 2=Emergency Overpressurizing enabled | If Emergency overpressurising is used, Water radiator Freezing protection is disabled! Emergency Overpressurizing should never be used in a room where fire is detected. |
| 3.0→ | 4x5207 | RW | Shutdown visibility in Smart functions | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in unit with User Panel |
| 3.0→ | 4x5004 | RW | Travelling mode | 0 | 1 | | 0=Travelling mode Disabled, 1=Travelling mode Enabled | All Smart functions are disabled |
| 3.0→ | 4x5106 | RW | Travelling mode speed drop | 0 | 20 | % | | |
| 3.0→ | 4x5202 | RW | Travelling visibility in Smart functions | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility |
| 3.0→ | 4x5002 | W | Fireplace function Activation | 0 | 1 | | 1=Activate Fireplace function with timer, 0=Stop Fireplace function | Fireplace function timer setting |
| 3.0→ | 4x5104 | RW | Fireplace function Run time | 0 | 60 | min | | |
| 3.0→ | 4x5105 | RW | Fireplace function Max fan speed difference | 0 | 25 | % | | |
| 3.0→ | 4x5201 | RW | Fireplace function visibility in Smart functions | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility |
| 3.0→ | 4x5005 | RW | Cooker Hood Damper Control | 0 | 1 | | 0=Cooker hood damper closed, 1=Cooker hood damper open | Open cooker hood damper and activates cooker hood function |
| 3.0→ | 4x5020 | RW | Cooker Hood function | 0 | 1 | | 0=Cooker hood function Disabled, 1=Cooker hood function Enabled | Cooker Hood function is activated when Casa cooker hood damper is opened |
| 3.0→ | 4x5109 | RW | Cooker Hood Home state compensation | 0 | 50 | % | | |
| 3.0→ | 4x5110 | RW | Cooker Hood Boost state compensation correction | 0 | 50 | % | | |
| 3.0→ | 4x5151 | RW | Cooker Hood Boost | 0 | 100 | % | Cooker Hood function minimum fan speed level | |
| 3.0→ | 4x5111 | RW | Cooker Hood Roof Fan Compensation | 0 | 1 | | 0=Cooker hood connected to unit extract duct, 1=Roof fan compensation | |
| 3.0→ | 4x5006 | RW | Central Vacuum Cleaner function | 0 | 1 | | 0=CVC mode Disabled, 1=CVC mode Enabled | |
| 3.0→ | 4x5112 | RW | Central Vacuum Cleaner run time | 0 | 60 | min | | RunTime is used only if function is activated manually from User Panel |
| 3.0→ | 4x5113 | RW | Central Vacuum Cleaner compensation | 0 | 50 | % | | |
| 3.0→ | 4x5204 | RW | Central Vacuum function visibility in Smart functions | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility |
| 3.0→ | 4x5009 | RW | Auto Home/Away/Boost control | 0 | 1 | | 0=Auto Home/Away/Boost control disabled, 1=Auto Home/Away/Boost control enabled | Available only in units with CO2 sensor |
| 3.0→ | 4x5114 | RW | Auto Home/Away/Boost Home Limit | 0 | 2000 | ppm | CO2 level when unit is working in home speed | |
| 3.0→ | 4x5115 | RW | Auto Home/Away/Boost Away Limit | 0 | 2000 | ppm | CO2 level when unit is working in away speed | |
| 3.1→ | 4x5010 | RW | Auto Humidity control | 0 | 5 | | 0=Off, 1=User, 2=Low, 3=Normal, 4=High, 5=Full | Available only in units with RH sensor (SW 3.1→) |
| 3.0 | 4x5010 | RW | Auto Humidity control | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with RH sensor (SW 3.0) |
| 3.0→ | 4x5117 | RW | Auto RH control Boost Limit | 0 | 50 | % | | Active if SW3.0 or User control selected |
| 3.0→ | 4x5118 | RW | Auto RH control Full Boost Limit | 0 | 50 | % | | Active if SW3.0 or User control selected |
| 3.1→ | 4x5119 | RW | Auto RH control Boost delay | 0 | 30 | min | Boost is delayed defined time | (SW 3.1→) |
| 3.1→ | 4x5120 | RW | Auto RH control Boost during delay | 0 | 25 | % | When boost delay is waited, fixed boost level can be defined | (SW 3.1→) |
| 3.0 | 4x5119 | RW | Auto RH control Sauna state | 0 | 1 | | 0=Sauna function Disabled, 1=Sauna function Enabled | (SW 3.0) |
| 3.0 | 4x5120 | RW | Auto RH control Sauna state fixed speed | 0 | 25 | % | When boost delay is waited, fixed boost level can be defined | (SW 3.0) |
| 3.1→ | 4x5208 | RW | Smart function visibility Auto Humidity Control | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility (SW 3.1→) |
| 3.0 | 4x5208 | RW | Smart automatic functions visibility | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility (SW 3.0) |
| 3.1→ | 4x5011 | RW | Auto Air Quality control | 0 | 5 | | 0=Off, 1=User, 2=Low, 3=Normal, 4=High, 5=Full | Available only in units with VOC sensor (SW 3.1→) |
| 3.0 | 4x5011 | RW | Auto Air Quality control | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with VOC sensor (SW 3.0) |
| 3.0→ | 4x5121 | RW | Auto Air Quality control Boost Limit | 0 | 2000 | ppm | | Active if SW3.0 or User control selected |
| 3.0→ | 4x5122 | RW | Auto Air Quality control Full Boost Limit | 0 | 2000 | ppm | | Active if SW3.0 or User control selected |
| 3.0→ | 4x5164 | RW | Summer Night Cooling control | 0 | 5 | | 0=Off, 1=Low, 2=Normal, 3=High, 4=Full, 5=User | |
| 3.0→ | 4x5165 | RW | Summer Cooling Fresh air temperature limit | 0 | 25 | °C | | |
| 3.0→ | 4x5166 | RW | Summer Cooling Fresh air temperature start limit | 0 | 25 | °C | Defines fresh air temperature when function is activated | Active if User control selected |
| 3.0→ | 4x5167 | RW | Summer Cooling Room temperature limit | 0 | 35 | °C | 0=Room temperature limit disabled, 18–28°C=function activated when room temperature is above limit | Active if User control selected |
| 3.0→ | 4x5168 | RW | Summer Cooling Minimum Supply temperature limit | 10 | 25 | °C | Supply temperature setpoint during the function | Active if User control selected |
| 3.0→ | 4x5177 | RW | Summer Cooling Open Cooker hood damper | 0 | 1 | | Control Cooker hood damper open when Summer night cooling is active | |
| 3.0→ | 4x5169 | RW | Summer Night Cooling Boost control | 0 | 5 | | 0=Off, 1=Low, 2=Normal, 3=High, 4=Full, 5=User | |
| 3.0→ | 4x5170 | RW | Summer Night Cooling Boost limit (room temperature) | 18 | 28 | °C | Ventilation is boosted when room temperature is higher than the limit | Active if User control selected |
| 3.1→ | 4x5125 | RW | Summer Night Cooling Full Boost limit (room temperature) | 18 | 40 | °C | Ventilation is boosted when room temperature is higher than the limit | Active if User control selected (SW 3.1→) |
| 3.0→ | 4x5205 | RW | Summer Night Cooling visibility in Smart functions | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in unit with User Panel |
| 3.0→ | 4x5012 | RW | Heating boost control | 0 | 1 | | 0=Disabled, 1=Enabled | Available only if Room temperature control selected |
| 3.0→ | 4x5124 | RW | Heating boost gain | 0 | 100 | % | Defines the boost level when room temperature is below setpoint | |
| 3.0→ | 4x5206 | RW | Smart function visibility Heating boost | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility |
| 3.0→ | 4x5101 | RW | Temperature setpoint | 13 | 25 | °C | Supply/Room temperature controller setpoint | Available only in units equipped with Re-heater or external Heating/Cooling device |
| 3.1→ | 4x5174 | RW | Heating Mode | 1 | 2 | | Supply temperature control: 1=ECO, 2=Comfort. If value is 0, Comfort mode NOT AVAILABLE for this unit | (SW 3.1→) |

## Airflow Adjustment

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 4x5029 | RW | Commissioning Mode | 0 | 9 | | 1=Travelling, 2=Away, 3=Home, 4=Boost, 5=MaxSmartBoost, 6=HoodHome, 7=HoodBoost, 8=HoodHoodBoost | Password protected — write 1234 before selection |
| 3.0→ | 4x5302 | RW | Away mode Supply fan speed | 20 | Home | % | fan speed | Don't use this register for external fan control |
| 3.0→ | 4x5303 | RW | Away mode Exhaust fan speed | 20 | Home | % | fan speed | Don't use this register for external fan control |
| 3.0→ | 4x5304 | RW | Home mode Supply fan speed | Away | Boost | % | fan speed | Don't use this register for external fan control |
| 3.0→ | 4x5305 | RW | Home mode Exhaust fan speed | Away | Boost | % | fan speed | Don't use this register for external fan control |
| 3.0→ | 4x5306 | RW | Boost mode Supply fan speed | Home | 100 | % | fan speed | Don't use this register for external fan control |
| 3.0→ | 4x5307 | RW | Boost mode Exhaust fan speed | Home | 100 | % | fan speed | Don't use this register for external fan control |
| 3.0→ | 4x5308 | RW | Max Smart boost limitation (% of Supply Boost) | 0 | 100 | % | Boost limitation. If 0% is selected, maximum Smart mode speed is Boost | |
| 3.0→ | 4x5311 | RW | Ventilation control mode | 0 | 5 | | 0=Normal, 1=PA Supply control, 2=PA Extract control, 3=PA control, 4=l/s control | If PA or l/s control is selected, commissioning must be done with User Panel |
| 3.0→ | 4x5312 | RW | Away mode Supply Pressure/Airflow | 0 | 255 | PA or l/s | Ventilation Pressure/Airflow setpoint | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0→ | 4x5313 | RW | Away mode Exhaust Pressure/Airflow | 0 | 255 | PA or l/s | Ventilation Pressure/Airflow setpoint | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0→ | 4x5314 | RW | Home mode Supply Pressure/Airflow | 0 | 255 | PA or l/s | Ventilation Pressure/Airflow setpoint | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0→ | 4x5315 | RW | Home mode Exhaust Pressure/Airflow | 0 | 255 | PA or l/s | Ventilation Pressure/Airflow setpoint | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0→ | 4x5316 | RW | Boost mode Supply Pressure/Airflow | 0 | 255 | PA or l/s | Ventilation Pressure/Airflow setpoint | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0→ | 4x5317 | RW | Boost mode Exhaust Pressure/Airflow | 0 | 255 | PA or l/s | Ventilation Pressure/Airflow setpoint | Commissioning must be done with User Panel in Commissioning Mode |

## GIO Modbus Control

**GIO function codes (registers 4x5157–4x5161):**

| Code | Function |
|---|---|
| 0 | Disabled |
| 1 | Emergency Stop NC (SW3.0) |
| 2 | Emergency Stop NO (SW3.0) / Emergency Stop (SW3.1→) |
| 3 | Stop |
| 4 | Fireplace |
| 5 | Cooker Hood |
| 6 | Central Vacuum Cleaner |
| 7 | Boost (force) |
| 8 | Away |
| 9 | Boost |
| 10 | Modbus |
| 11 | Relay control |
| 12 | Resettable Emergency Stop (SW3.1→) |
| 13 | External Alarm (SW3.1→) |
| 64 | AI: Mode control |
| 65 | AI: Smart Control |
| 66 | AI: Modbus |
| 67 | AI: Pa (supply) |
| 68 | AI: Pa (extract) |
| 69 | AI: Airflow (supply) |
| 70 | AI: Airflow (exhaust) |
| 71 | AI: RH |
| 72 | AI: CO2 |
| 73 | AI: VOC |
| 128 | DO: Alarm |
| 129 | DO: Duct Damper |
| 130 | DO: Away state |
| 131 | DO: Boost state |
| 132 | DO: Modbus |
| 133 | DO: DI control |
| 134 | DO: Manual ON |
| 135 | DO: Travelling (SW3.1→) |
| 136 | DO: Stop (SW3.1→) |
| 137 | DO: Service (SW3.1→) |
| 138 | DO: Critical Alarm (SW3.1→) |

**SET Relay function codes (registers 4x5162–4x5163):**

| Code | Function |
|---|---|
| 0 | NA |
| 1 | Heating |
| 2 | Cooling |
| 3 | Ground Liquid pump |
| 4 | Duct Plate |
| 5 | Floor Heating |
| 6 | Alarm |
| 7 | Away |
| 8 | Boost |
| 9 | DI-controlled |
| 10 | Modbus controlled |

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 4x5021 | RW | GIO1 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO1 Type Relay Output and Function Modbus (4x5157=132) |
| 3.0→ | 4x5022 | RW | GIO2 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO2 Type Relay Output and Function Modbus (4x5158=132) |
| 3.0→ | 4x5023 | RW | GIO3 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO3 Type Relay Output and Function Modbus (4x5159=132) |
| 3.0→ | 4x5024 | RW | GIO4 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO4 Type Relay Output and Function Modbus (4x5160=132) |
| 3.0→ | 4x5025 | RW | GIO5 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO5 Type Relay Output and Function Modbus (4x5161=132) |
| 3.0→ | 3x6349 | R | GIO 1 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO1 Type Switch Input and Modbus (4x5157=10) |
| 3.0→ | 3x6350 | R | GIO 2 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO2 Type Switch Input and Modbus (4x5158=10) |
| 3.0→ | 3x6351 | R | GIO 3 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO3 Type Switch Input and Modbus (4x5159=10) |
| 3.0→ | 3x6352 | R | GIO 4 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO4 Type Switch Input and Modbus (4x5160=10) |
| 3.0→ | 3x6353 | R | GIO 5 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO5 Type Switch Input and Modbus (4x5161=10) |
| 3.0→ | 3x6354 | R | GIO 1 AI value | 0 | 10000 | mV | | Select IO1 Type Voltage in and Function Modbus (4x5157=66) |
| 3.0→ | 3x6355 | R | GIO 2 AI value | 0 | 10000 | mV | | Select IO2 Type Voltage in and Function Modbus (4x5158=66) |
| 3.0→ | 3x6356 | R | GIO 3 AI value | 0 | 10000 | mV | | Select IO3 Type Voltage in and Function Modbus (4x5159=66) |
| 3.0→ | 3x6357 | R | GIO 4 AI value | 0 | 10000 | mV | | Select IO4 Type Voltage in and Function Modbus (4x5160=66) |
| 3.0→ | 3x6358 | R | GIO 5 AI value | 0 | 10000 | mV | | Select IO5 Type Voltage in and Function Modbus (4x5161=66) |
| 3.0→ | 4x5157 | RW | GIO 1 function | 0 | 255 | | See GIO function codes above | |
| 3.0→ | 4x5158 | RW | GIO 2 function | 0 | 255 | | See GIO function codes above | |
| 3.0→ | 4x5159 | RW | GIO 3 function | 0 | 255 | | See GIO function codes above | |
| 3.0→ | 4x5160 | RW | GIO 4 function | 0 | 255 | | See GIO function codes above | |
| 3.0→ | 4x5161 | RW | GIO 5 function | 0 | 255 | | See GIO function codes above | |
| 3.1→ | 4x5173 | RW | GIO Activation NO/NC | 0 | 255 | bit | BIT0=GIO1, BIT1=GIO2, BIT2=GIO3, BIT3=GIO4, BIT5=GIO5 (0=Activate when Closed, 1=Activate when Open) | GIO Polarity (SW 3.1→) |
| 3.0→ | 4x5026 | RW | SET Relay 1 output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select SET Relay 1 Modbus (4x5162=8) |
| 3.0→ | 4x5027 | RW | SET Relay 2 output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select SET Relay 2 Modbus |
| 3.0→ | 4x5028 | RW | AO4 Output control | 0 | 100 | 0.01V | AO4 Voltage output control | Select AO4 Function to Modbus (4x5172=4) |
| 3.0→ | 4x5162 | RW | SET Relay 1 function | 0 | 255 | | See SET Relay function codes above | |
| 3.0→ | 4x5163 | RW | SET Relay 2 function | 0 | 255 | | See SET Relay function codes above | |
| 3.1→ | 4x5172 | RW | AO4 Output type | 0 | 35 | | 0=NA, 1=Control, 2=Stepless Control, 3=Temp SP, 4=Modbus | (SW 3.1→) |

## Heating / Cooling

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 4x5130 | RW | Temperature Controller method | 0 | 1 | | 0=Supply air, 1=Room air | |
| 3.0→ | 4x5101 | RW | Temperature setpoint | 16 | 23 | °C | Supply/Room temperature controller setpoint | Available only in units equipped with Heating/Cooling device |
| 3.0→ | 4x5107 | RW | Travelling mode temperature drop | 0 | 10 | °C | Temperature drop of Setpoint | |
| 3.0→ | 4x5171 | RW | Away State Temperature Drop | 0 | 10 | °C | Temperature drop of Setpoint | |
| 3.0→ | 4x5133 | RW | Room Control, Supply control min | 10 | 50 | °C | | Available only if Room temperature control selected |
| 3.0→ | 4x5134 | RW | Room Control, Supply control max | 10 | 50 | °C | | Available only if Room temperature control selected |
| 3.0→ | 4x5136 | RW | Room Control, Cooling control min | 10 | 50 | °C | | Available only in units with External Cooling device |
| 3.0→ | 4x5137 | RW | Room Control, Cooling control max | 10 | 50 | °C | | Available only in units with External Cooling device |
| 3.1→ | 4x5174 | RW | Heating Mode | 0 | 2 | | Supply temperature control: 1=ECO, 2=Comfort. If value is 0, Comfort mode NOT AVAILABLE for this unit | (SW 3.1→) |
| 3.0→ | 4x5014 | RW | Internal Post heater | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with controlled re-heater |
| 3.0→ | 4x5016 | RW | External Post heater | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with External Heating device |
| 3.0→ | 4x5129 | RW | Heating Fresh air limit | -50 | 50 | °C | Fresh air limit when heating allowed | Available only in units with controlled re-heater |
| 3.0→ | 4x5015 | RW | External Cooling control | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with External Cooling device |
| 3.0→ | 4x5135 | RW | Cooling Fresh air limit | 0 | 50 | °C | | Available only in units with External Cooling device |
| 3.0→ | 4x5017 | RW | External liquid coil (preheating / cooling) | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with External preheater/cooling device |
| 3.0→ | 4x5138 | RW | External Pre Heating Fresh air limit | -50 | 50 | °C | | Available only in units with External preheater/cooling device |
| 3.0→ | 4x5139 | RW | External Pre Cooling Fresh air limit | -50 | 50 | °C | | Available only in units with External preheater/cooling device |
| 3.0→ | 4x5176 | RW | External Electrical Preheater | 0 | 1 | | 0=Disabled, 1=Enabled | Available only in units with External electrical preheater |
| 3.0→ | 4x5152 | RW | Room Temperature Sensor | 0 | 6 | | 0=Internal, 1=T6, 2=T7, 3=T8, 4=T9, 5=UP1, 6=UP2 | |
| 3.0→ | 4x5132 | RW | Room Temperature Fine Tuning | -50 | 50 | 0.1°C | Room Temperature fine tuning | |
| 3.0→ | 4x5153 | RW | Supply Temperature Sensor | 0 | 4 | | 0=Internal, 1=T6, 2=T7, 3=T8, 4=T9 | |
| 3.0→ | 4x5155 | RW | Supply Temperature Fine Tuning | -50 | 50 | 0.1°C | Supply temperature fine tuning | |
| 3.0→ | 4x5154 | RW | Outside Temperature Sensor | 0 | 4 | | 0=Internal, 1=T6, 2=T7, 3=T8, 4=T9 | |
| 3.0→ | 4x5156 | RW | Water Temperature Sensor | 0 | 4 | | 0=Internal, 1=T6, 2=T7, 3=T8, 4=T9 | If sensor selected, Freezing prevention function is activated |

## Alarms

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 4x5141 | RW | Service Reminder | 0 | 1 | | 0=Disabled, 1=Enabled | Service time can be reset by writing 0 and then 1 to this register |
| 3.0→ | 4x5142 | RW | Service Reminder interval | 0 | 12 | months | | |
| 3.0→ | 3x6129 | R | Service Info | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6136 Bit 9 |
| 3.0→ | 4x5406 | W | Reset All info alarms | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5401 | W | Re-heater failure alarm confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5402 | W | Preheater failure alarm confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5403 | W | Water radiator Freezing danger alarm confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5404 | W | Filter Guard info confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5405 | W | Service Timer info confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5407 | W | Fan failure alarm confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 4x5408 | W | Sensor failure confirm | 0 | 1 | | 1=Confirm Alarm. Register is cleared when command is processed. | |
| 3.0→ | 3x6136 | R | Active Alarms Bitwise | 0 | 16bit | | See alarm bit description below. 0=No Alarm, 1=Active alarm | |
| 3.0→ | 3x6137 | R | Unconfirmed Info Bitwise | 0 | 16bit | | See alarm bit description below. 0=No info, 1=Unconfirmed Info alarm | |
| 3.0→ | 3x6132 | R | Active Alarms | 0 | 1 | | 0=No Alarms, 1=Active Alarm | |
| 3.0→ | 3x6133 | R | Unconfirmed Info | 0 | 1 | | 0=No Info, 1=Active Info | |
| 3.0→ | 3x6101 | R | T1 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6102 | R | T2 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6103 | R | T3 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6104 | R | T4 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6105 | R | T5 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6106 | R | T6 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6107 | R | T7 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6108 | R | T8 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 6 |
| 3.0→ | 3x6134 | R | T9 Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | |
| 3.0→ | 3x6109 | R | T1 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6110 | R | T2 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6111 | R | T3 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6112 | R | T4 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6113 | R | T5 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6114 | R | T6 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6115 | R | T7 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6116 | R | T8 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 6 |
| 3.0→ | 3x6135 | R | T9 Unconfirmed Temperature Sensor Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | Alarm is automatically confirmed |
| 3.0→ | 3x6117 | R | Afterheater failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 0 |
| 3.0→ | 3x6118 | R | Unconfirmed Afterheater failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 0 |
| 3.0→ | 3x6119 | R | Preheater failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 1 |
| 3.0→ | 3x6120 | R | Unconfirmed Preheater failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 1 |
| 3.0→ | 3x6121 | R | Freezing danger | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 3 |
| 3.0→ | 3x6122 | R | Unconfirmed Freezing danger | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 3 |
| 3.0→ | 3x6123 | R | Internal Temperature | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 10 |
| 3.0→ | 3x6124 | R | Unconfirmed Internal Temperature | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 10 |
| 3.0→ | 3x6125 | R | Supply Fan Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 4 |
| 3.0→ | 3x6126 | R | Unconfirmed Supply Fan Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 4 |
| 3.0→ | 3x6127 | R | Exhaust Fan Failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 5 |
| 3.0→ | 3x6128 | R | Unconfirmed Exhaust Fan Failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 5 |
| 3.0→ | 3x6130 | R | Filter guard info | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 8 |
| 3.0→ | 3x6131 | R | Emergency Stop | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6137 Bit 7 |
| 3.0→ | 3x6143 | R | Supply temperature low alarm | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 11 |
| 3.0→ | 3x6144 | R | Unconfirmed Supply temperature low alarm | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 11 |
| 3.0→ | 3x6145 | R | Supply temperature high alarm | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 12 |
| 3.0→ | 3x6146 | R | Unconfirmed Supply temperature high alarm | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 12 |
| 3.0→ | 3x6141 | R | Preheater temperature high alarm | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 13 |
| 3.0→ | 3x6142 | R | Unconfirmed Preheater temperature high alarm | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 13 |
| 3.1→ | 3x6119 | R | External Preheater failure | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 2 |
| 3.1→ | 3x6120 | R | Unconfirmed External Preheater failure | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 2 |
| 3.1→ | 3x6147 | R | Rotor alarm | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 14 |
| 3.1→ | 3x6148 | R | Unconfirmed Rotor alarm | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 14 |
| 3.0→ | 3x6149 | R | Fan Control alarm | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 15 |
| 3.1→ | 3x6150 | R | Unconfirmed Fan Control alarm | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6137 Bit 15 |

## Device Information

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 3x6001 | R | Device Firmware version major | 0 | 99 | | | |
| 3.0→ | 3x6002 | R | Device Firmware version minor | 0 | 99 | | | |
| 3.0→ | 3x6003 | R | Device Firmware build | 0 | 999 | | | |
| 3.0→ | 3x6004 | R | Parameter version major | 0 | 99 | | | |
| 3.0→ | 3x6005 | R | Parameter version minor | 0 | 99 | | | |
| 3.0→ | 3x6008 | R | Model name [0:14] | — | — | ASCII | Model name ASCII code | Registers 3x6008–3x6024 |
| 3.0→ | 3x6024 | R | Unit Serial Number [0:23] | — | — | ASCII | Unit serial number ASCII code. Direct access to Service Portal. | Registers 3x6024–3x6047 |

## Diagnostics — Measurements

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 3x6201 | R | Fresh air temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6202 | R | Supply air before re-heater temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6203 | R | Supply air temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6204 | R | Extract air temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6205 | R | Exhaust (waste) air temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6206 | R | Room air temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6207 | R | User Panel 1 temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6208 | R | User Panel 2 temperature | -550 | 600 | 0.1°C | | |
| 3.0→ | 3x6209 | R | Water Radiator temperature | -550 | 600 | 0.1°C | | Available only in units with water radiator |
| 3.0→ | 3x6210 | R | Pre-heater temperature | -550 | 600 | 0.1°C | | Available only in units with Preheater |
| 3.0→ | 3x6211 | R | External Fresh air temperature | -550 | 600 | 0.1°C | | Only if External PreHeater/Cooling selected |
| 3.0→ | 3x6212 | R | CO2 Unfiltered | 0 | 2000 | ppm | | Available only in units with CO2 sensor |
| 3.0→ | 3x6213 | R | CO2 Filtered | 0 | 2000 | ppm | | Available only in units with CO2 sensor |
| 3.0→ | 3x6214 | R | RH | 0 | 100 | % | | Available only in units with RH sensor |
| 3.0→ | 3x6215 | R | AH | 0 | 5000 | 0.1 g/m³ | | Available only in units with RH sensor |
| 3.0→ | 3x6216 | R | AH SetPoint | 0 | 5000 | 0.1 g/m³ | | Available only in units with RH sensor |
| 3.0→ | 3x6217 | R | VOC | 0 | 2000 | ppm | | Available only in units with VOC sensor |
| 3.0→ | 3x6218 | R | Supply Duct Pressure | 0 | 500 | Pa | | |
| 3.0→ | 3x6219 | R | Exhaust Duct Pressure | 0 | 500 | Pa | | |
| 3.0→ | 3x6220 | R | Supply Air Flow | 0 | 500 | l/s | | |
| 3.0→ | 3x6221 | R | Exhaust Air Flow | 0 | 500 | l/s | | |

## Diagnostics — Unit Status

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0→ | 3x6301 | R | Unit state | 0 | 4 | | 0=External Stop, 1=User Stopped, 2=Starting, 3=Normal, 4=Commissioning | |
| 3.0→ | 3x6302 | R | Ventilation Speed state | 0 | 4 | | 0=Stopped, 1=Away, 2=Home, 3=Boost | |
| 3.0→ | 3x6303 | R | Supply Fan Control | 0 | 100 | % | | |
| 3.0→ | 3x6304 | R | Exhaust Fan Control | 0 | 100 | % | | |
| 3.0→ | 3x6305 | R | Supply Fan RPM | 0 | — | 1/min | | |
| 3.0→ | 3x6306 | R | Exhaust Fan RPM | 0 | — | 1/min | | |
| 3.0→ | 3x6234 | R | Rotor RPM | 0 | — | 1/min | | |
| 3.0→ | 3x6307 | R | Travelling Function Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6308 | R | Boost Time left | 0 | 120 | min | Timed Function remaining time | |
| 3.0→ | 3x6309 | R | Week Timer Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6310 | R | A+ Control | -100 | 100 | % | | Available only in units with CO2 sensor |
| 3.0→ | 3x6311 | R | Auto RH Control | 0 | 100 | % | | Available only in units with RH sensor |
| 3.0→ | 3x6312 | R | Auto Air Quality Control | 0 | 100 | % | | Available only in units with VOC sensor |
| 3.0→ | 3x6313 | R | Auto Temperature Boost Control | 0 | 100 | % | | Available only if Room temperature control selected |
| 3.0→ | 3x6314 | R | Fan Speed limit Control | -100 | 0 | % | | |
| 3.0→ | 3x6315 | R | Smart Control | -100 | 100 | % | | |
| 3.0→ | 3x6316 | R | Temperature Setpoint | 13 | 25 | °C | | Available only in units with controlled re-heater |
| 3.0→ | 3x6317 | R | Supply Control Power output | 0 | 100 | % | Heating or Cooling Output control | Available only in units with controlled re-heater / cooling |
| 3.0→ | 3x6320 | R | Room Controller Supply Setpoint | 0 | 50 | 0.1°C | | Available only if Room temperature control selected |
| 3.0→ | 3x6323 | R | Cooling Control Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | See 3x16317 for Cooling power |
| 3.0→ | 3x6328 | R | Defrost Active | 0 | 4 | | 0=Function Not Active, 1–4=Defrost Function Active | |
| 3.0→ | 3x6332 | R | Rotor Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | Available only in R-Series Units |
| 3.0→ | 3x6333 | R | Preheater Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | Available only in units with Preheater |
| 3.0→ | 3x6334 | R | Summer Cooling Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6335 | R | Fireplace function Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6336 | R | Central Vacuum Cleaner function active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6337 | R | Hood Compensation Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6338 | R | External Boost Control Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6339 | R | External Away Control Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0→ | 3x6340 | R | Manual Heat Exchanger bypass plate Position | 0 | 2 | | 0=Heat Exchanger bypass plate Closed (Winter), 1=Heat Exchanger bypass plate Open (Summer) | Available only in units with Manual Heat Exchanger |
| 3.0→ | 3x6348 | R | Automatic Heat Exchanger bypass plate Position | 0 | 100 | % | 100% is completely open | Available only in units with Automatic Heat Exchanger |
| 3.0→ | 3x6342 | R | Filter Guard Input status | 0 | 1 | | 0=Filter Guard input Not Active, 1=Filter Guard input Active | |
| 3.0→ | 3x6343 | R | Hours to next Service | 0 | 10000 | hours | | Available if Service Reminder enabled (see 4x5142 for Service Interval) |
| 3.0→ | 3x6344 | R | Preheater Output Power | 0 | 100 | % | | |
| 3.0→ | 3x6345 | R | Nordic Preheater Power | 0 | 100 | % | | |
| 3.0→ | 3x6346 | R | Defrost Supply limit | 0 | 100 | % | | |
| 3.0→ | 3x6347 | R | Defrost exhaust forcing | 0 | 100 | % | | |
