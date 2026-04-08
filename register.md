# Swegon CASA Genius Modbus Register

**SCB 4.1** — Note: This register list is only valid for SEM / SEC modbus connection with SW4.0 Genius software. Updated 230828.

## USER SETTINGS

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 4x5001 | RW | Operating Mode | 0 | 5 | | 0=Shutdown, 1=Away, 2=Home, 3=Boost, 4=Travelling, 5=Home+ (SW4.0 Genius) | |
| 3.0-> | 4x5102 | RW | Boost mode timer | 0 | 5 | | 0=Continuous, 1=30min, 2=60min, 3=90min, 4=120min, 5=240min | |
| 4.0-> | 4x5108 | RW | Home+ mode ventilation level | 10 | 90 | % | 0% corresponds to the Home mode and 100% the Boost mode ventilation level | |
| 4.0-> | 4x5203 | RW | Home+ visibility in User Panel | 0 | 1 | | 0=Not visible/disabled, 1=Enabled | User Panel visibility |
| 3.0-> | 4x5106 | RW | Travelling mode speed drop | 0 | 10 | % | Traveling mode ventilation reduction from away mode | |
| 3.0-> | 4x5202 | RW | Travelling visibility in User Panel | 0 | 1 | | 0=Not visible/disabled, 1=Enabled | User Panel visibility |
| 3.0-> | 4x5207 | RW | Shutdown visibility in User Panel | 0 | 1 | | 0=Not visible/disabled, 1=Enabled | User Panel visibility |
| 3.0-> | 4x5018 | RW | Emergency Stop | 0 | 2 | | 0=Emergency stop disabled, 1=Emergency stop enabled, 2=Emergency Overpressurizing enabled | If Emergency overpressurising is used, Water radiator Freezing protection is disabled! |
| 3.0-> | 4x5009 | RW | CO2 automation | 0 | 1 | | 0=Auto Home/Away/Boost control disabled, 1=Auto Home/Away/Boost control enabled | Available only in units with CO2 sensor |
| 4.0-> | 4x5116 | RW | Boost mode Limit | 0 | 2000 | ppm | CO2 level when unit is working in boost speed | |
| 3.0-> | 4x5114 | RW | Home mode Limit | 0 | 2000 | ppm | CO2 level when unit is working in home speed | |
| 3.0-> | 4x5115 | RW | Away mode Limit | 0 | 2000 | ppm | CO2 level when unit is working in away speed | |
| 3.1-> | 4x5010 | RW | RH automation | 0 | 5 | | 0=Off, 1=Low, 2=Normal, 3=High, 4=Max, 5=Advanced | |
| 4.0-> | 4x5010-1 | | - Low selection | | | | Max boost level is 1/3 of Home-Boost level. Boost limit is 10% + RH average and full boost limit is 40% + RH average | |
| 4.0-> | 4x5010-2 | | - Normal selection | | | | Max boost level is 2/3 of Home-Boost level. Boost limit is 5% + RH average and full boost limit is 30% + RH average | |
| 4.0-> | 4x5010-3 | | - High selection | | | | Max boost level is Boost level. Boost limit is 5% + RH average and full boost limit is 20% + RH average | |
| 4.0-> | 4x5010-4 | | - Full selection | | | | Max boost level is Boost level. Boost limit is 5% and boosting is set immediately to max | |
| 4.0-> | 4x5117 | RW | - Advanced selection Boost Limit | 0 | 50 | % | The ventilation is boosted steplessly when the humidity has risen from the average Boost limit defined amount | |
| 4.0-> | 4x5118 | RW | - Advanced selection Max Boost Limit | 0 | 50 | % | The maximum ventilation boost is reached when the humidity has risen the full boost limit defined amount from the average | |
| 4.0-> | 4x5178 | RW | - Advanced selection Max allowed boost level | 0 | 100 | % | 0% corresponds to the Home mode and 100% the Boost mode ventilation level | |
| 3.1-> | 4x5119 | RW | Boost delay | 0 | 30 | min | Boost start is delayed so that ventilation is not disturbing during the shower | |
| 3.1-> | 4x5120 | RW | Boost during delay | 0 | 25 | % | Boost delay during the delay | |
| 4.0-> | 4x5179 | RW | Automation allowed in away mode | 0 | 1 | | Allow function in away mode | |
| 3.0 | 4x5011 | RW | VOC automation | 0 | 1 | | 0=Off, 1=Low, 2=Normal, 3=High, 4=Max, 5=Advanced | Available only in units with VOC sensor |
| 4.0-> | 4x5011-1 | RW | - Low selection | | | | Max boost level is 1/3 of Home-Boost level. Boost limit is 1200ppm and full boost limit is 2000ppm | |
| 4.0-> | 4x5011-2 | RW | - Normal selection | | | | Max boost level is 2/3 of Home-Boost level. Boost limit is 800ppm and full boost limit is 2000ppm | |
| 4.0-> | 4x5011-3 | RW | - High selection | | | | Max boost level is Boost level. Boost limit is 700ppm and full boost limit is 1500ppm | |
| 4.0-> | 4x5011-4 | RW | - Full selection | | | | Max boost level is Boost level. Boost limit is 500ppm and full boost limit is 1000ppm | |
| 3.0-> | 4x5121 | RW | - Advanced selection Boost limit | 0 | 2000 | ppm | The boost starts when the room temperature is over the set limit. Summer mode needs to be active and supply temperature cold enough | |
| 3.0-> | 4x5122 | RW | - Advanced selection Full boost limit | 0 | 2000 | ppm | Temperature limit when boost is in max level | |
| 4.0-> | 4x5180 | RW | - Advanced selection Max allowed boost level | 0 | 100 | % | 0% corresponds to the Home mode and 100% the Boost mode ventilation level | |
| 4.0-> | 4x5181 | RW | Automation allowed in away mode | 0 | 1 | | Allow function in away mode | |
| 4.0-> | 4x5169 | RW | Summer mode boost | 0 | 5 | | 0=Off, 1=Low, 2=Normal, 3=High, 4=Max, 5=Advanced | |
| 4.0-> | 4x5169-1 | RW | - Low selection | | | | Max boost level is Home level. Boost gain: 6°C room temperature difference -> Max boost | |
| 4.0-> | 4x5169-2 | RW | - Normal selection | | | | Max boost level is 1/2 of Home-Boost level. Boost gain: 4°C room temperature difference -> Max boost | |
| 4.0-> | 4x5169-3 | RW | - High selection | | | | Max boost level is Boost level. Boost gain: 2°C room temperature difference -> Max boost | |
| 4.0-> | 4x5169-4 | RW | - Full selection | | | | Max boost level is Boost level. Boost gain: 1°C room temperature difference -> Max boost | |
| 3.0-> | 4x5170 | RW | Advanced selection Boost limit (room temperature) | 130 | 300 | 0.1°C | Ventilation is boosted when room temperature is higher than the limit | |
| 3.1-> | 4x5125 | RW | Advanced selection Full Boost limit (room temperature) | 130 | 300 | 0.1°C | Ventilation is boosted to maximum when room temperature reaches the limit | |
| 4.0-> | 4x5182 | RW | Advanced selection Max allowed boost level | 0 | 100 | % | 0% corresponds to the Home mode and 100% the Boost mode ventilation level | |
| 4.0-> | 4x5183 | RW | Automation allowed in away mode | 0 | 1 | | Allow function in away mode | |
| 3.0-> | 4x5005 | RW | Cooking mode control | 0 | 1 | | 0=Cooker hood damper is closed, 1=Cooker hood damper is opened and cooking mode airflows are activated. 10h timer is activated | Open cooker hood damper and activates cooking mode. Modbus control has 10 hour timer so function is active 10h or when controlled off or if unit is restarted |
| 3.0-> | 4x5020 | RW | Cooker hood selection | 0 | 4 | | 0=No Cooker hood, 1=Cooker hood function with ventilation unit, 2=Cooker hood with roof fan, 3=Cooker hood with integrated fan, 4=Recirculating cooker hood | Cooker Hood function is activated when Casa cooker hood damper is opened |
| 4.0-> | 4x5184 | RW | Cooking mode Supply fan control | 20 | 100 | % | Measure building internal pressure and select supply fan control so that pressure is in balance | |
| 4.0-> | 4x5185 | RW | Cooking mode Extract fan control | 20 | 100 | % | Measure building internal pressure and select extract fan control so that pressure is in balance | |
| 3.0-> | 4x5002 | W | Fireplace function Activation | 0 | 1 | | 1=Activate Fireplace function with timer, 0=Stop Fireplace function | Fireplace function activation |
| 4.0-> | 4x5105 | RW | Fireplace function level | 0 | 2 | | 0=Low (1/3 of max), 1=Normal (2/3 of max), 2=High (max) | Overpressure level |
| 3.0-> | 4x5201 | RW | Fireplace function visibility in User Panel | 0 | 1 | | 0=Disabled, 1=Enabled | User Panel visibility |
| 4.0-> | | | Central Vacuum Cleaner (CVC) function | | | | Control only with CVC input | |
| 3.0-> | 4x5113 | RW | Central Vacuum Cleaner compensation | 0 | 50 | % | Fan speed compensation activated with IO input. Decrease Exhaust fan speed (Min speed Away) and increase supply fan speed if necessary | |

## Heating / Cooling

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 4x5101 | RW | Temperature setpoint | 130 | 250 | 0.1°C | Supply temperature setpoint (Supply air control method = Supply air) | |
| 4.0-> | 4x5168 | RW | Temperature setpoint Summer | 130 | 250 | 0.1°C | Supply temperature setpoint for summer period | |
| 4.0-> | 4x5164 | RW | Summer mode detection | 0 | 2 | | 0=OFF, 1=Auto, 2=ON | |
| 4.0-> | 4x5166 | RW | Summer mode detection outside limit | 0 | 400 | 0.1°C | Summer mode is detected when outside temperature or outside average temperature is above limit | |
| 4.0-> | 4x5167 | RW | Summer mode Room temperature limit | 100 | 400 | 0.1°C | Summer mode is detected when room temperature is above limit | Active if User control selected |
| 4.0-> | 4x5186 | RW | Winter mode limit | -100 | 300 | 0.1°C | Winter mode is activated when outside temperature is below the limit. Heat exchanger is controlled to maximum heating efficiency | |
| 4.0-> | 4x5107 | RW | Winter mode Supply temperature setpoint for Away | 130 | 250 | 0.1°C | | Save energy on the heating period in away mode by selecting a lower supply air temperature setpoint |
| 4.0-> | 4x5171 | RW | Winter mode Supply temperature setpoint for Travelling | 130 | 250 | 0.1°C | | Save energy on the heating period in travelling mode by selecting a lower supply air temperature setpoint |
| 3.0-> | 4x5130 | RW | Supply air control method | 0 | 1 | | 0=Supply air, 1=Room air | |
| 4.0-> | 4x5187 | RW | Room temperature setpoint | 130 | 250 | 0.1°C | Supply/Room temperature controller setpoint | |
| 4.0-> | 4x5188 | RW | Winter mode Room temperature setpoint for Away | 130 | 250 | 0.1°C | | Save energy on the heating period in away mode by selecting a lower room air temperature setpoint |
| 4.0-> | 4x5189 | RW | Winter mode Room temperature setpoint for Travelling | 130 | 250 | 0.1°C | | Save energy on the heating period in travelling mode by selecting a lower room air temperature setpoint |
| 3.0-> | 4x5133 | RW | Room air control, Min Supply temperature setpoint | 130 | 250 | 0.1°C | | Room air control method controls the supply temperature setpoint between selected setpoint limits based on room temperature |
| 3.0-> | 4x5134 | RW | Room air control, Max Supply temperature setpoint | 130 | 250 | 0.1°C | | |
| 3.0-> | 4x5136 | RW | Room air control (cooling), Min Supply temperature setpoint | 10 | 50 | 0.1°C | | If external cooling coil is installed, the room air control method controls the supply temperature setpoint between selected limits when cooling is active. Available only if Room temperature control selected with External Cooling device |
| 3.0-> | 4x5137 | RW | Room air control (cooling), Max Supply temperature setpoint | 10 | 50 | 0.1°C | | Available only if Room temperature control selected with External Cooling device |

## Duct Coils

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 4.0-> | | | Internal Post heater | | | | Use outside temperature limit to disable internal postheater | Available only in units with internal postheater |
| 3.0-> | 4x5129 | RW | Heating Fresh air limit | -50 | 300 | 0.1°C | Heating is allowed when outside temperature is below the limit | Available only in units with internal postheater |
| 4.0-> | 4x5016 | RW | External Post heater Liquid / Electrical | 0 | 1 | | 0=Disabled, 1=Water based post heater, 2=Electrical post heater | Available only in units with External Heating device |
| 3.0-> | 4x5129 | RW | Heating Fresh air limit | -50 | 50 | °C | Heating is allowed when outside temperature is below the limit | |
| 3.0-> | 4x5153 | RW | T7 External Supply Temperature Sensor | 0 | 1 | | 0=Swegon PTC, 1=PT1000 | Must be installed if external postheater is installed |
| 3.0-> | 4x5156 | RW | T6 Water Temperature Sensor Type | 0 | 1 | | 0=Swegon PTC, 1=PT1000 | Must be installed if water based postheater is installed |
| 4.0-> | 4x5015 | RW | External Post Cooling control / Ground liquid cooling | 0 | 1 | | 0=Disabled, 1=Liquid based post cooler, 2=Water based post cooler | Available only in units with External Cooling device |
| 3.0-> | 4x5135 | RW | Cooling Fresh air limit | 0 | 50 | °C | Cooling is allowed when outside temperature is above the limit | Available only in units with External Cooling device |
| 4.0-> | 4x5153 | RW | T7 External Supply Temperature Sensor | 0 | 1 | | 0=Swegon PTC, 1=PT1000 | Must be installed if external post cooler is installed |
| 4.0-> | 4x5156 | RW | T6 Water Temperature Sensor Type | 0 | 1 | | 0=Swegon PTC, 1=PT1000 | Must be installed if water based post cooler is installed |
| 3.0-> | 4x5017 | RW | External liquid coil (preheating / cooling) | 0 | 1 | | 0=Disabled, 1=Enabled. Define Relay output (DO) for Liquid preheater/precooler pump before enabling. Function controls pump/valve relay based on outside temperature | |
| 3.0-> | 4x5138 | RW | External Pre heating Fresh air limit | -50 | 50 | °C | Output for Preheating/cooling is activated when outside temperature is below the limit | Available only in units with External preheater/cooling device |
| 3.0-> | 4x5139 | RW | External Pre cooling Fresh air limit | -50 | 50 | °C | Output for Preheating/cooling is activated when outside temperature is above the limit | Available only in units with External preheater/cooling device |
| 4.0-> | 4x5154 | RW | T8 External Outside Temperature Sensor | 0 | 1 | | 0=Swegon PTC, 1=PT1000 | External outside temperature measurement is used for external preheater/cooler output control |
| 4.0-> | 4x5176 | RW | External Preheater Liquid / Electrical | 0 | 1 | | 0=Disabled, 1=Electrical preheater, 2=Liquid based preheater | Available only in units with External preheater |

## External Connections

GIO function values: Disabled=0; DI: 1=Emergency Stop, 2=Emergency Stop Resetted, 3=Stop, 4=Travelling, 5=Away, 6=Away/Home, 7=Home, 8=Home+, 9=Boost, 10=Boost(pulse), 11=Fireplace(pulse), 12=Cooking mode, 13=Central vacuum cleaner compensation, 14=Fire alarm, 15=External device message, 16=External device Alarm, 17=External device critical alarm, 18=Modbus input, 19=Output control, 20=Max Cooling; AI: 64=Mode control, 65=Stepless mode Control, 66=Modbus measurement, 67=Pa(supply), 68=Pa(extract), 69=Airflow(supply), 70=Airflow(exhaust), 71=RH, 72=CO2, 73=VOC, 74=Temperature, 75=Room pressure, 76=Outside humidity, 77=Supply air humidity; DO: 129=Test/User panel controlled, 130=Duct Damper, 131=Alarm, 132=Service, 133=Critical Alarm, 134=User stopped, 135=Unit is running, 136=Travelling, 137=Away, 138=Home, 139=Home+, 140=Boost, 141=Fireplace, 142=Humidity boost, 143=Modbus output, 144=Input controlled output, 145=Heating active, 146=Cooling active, 147=Liquid Preheater/cooler active, 148=External Heating circuit, 149=Internal Cooling

SET Relay function values: 1=Test/User panel controlled, 2=Duct Damper, 3=Alarm, 4=Service, 5=Critical Alarm, 6=User stopped, 7=Unit is running, 8=Travelling, 9=Away, 10=Home, 11=Home+, 12=Boost, 13=Fireplace, 14=Humidity boost, 15=Modbus output, 16=Input controlled output, 17=Heating active, 18=Cooling active, 19=Preheater/cooler active, 20=External Heating circuit, 21=Internal Cooling

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 4x5157 | RW | GIO 1 function | 0 | 255 | | See GIO function values above | |
| 3.0-> | 4x5158 | RW | GIO 2 function | 0 | 255 | | See GIO function values above | |
| 3.0-> | 4x5159 | RW | GIO 3 function | 0 | 255 | | See GIO function values above | |
| 3.0-> | 4x5160 | RW | GIO 4 function | 0 | 255 | | See GIO function values above | |
| 3.0-> | 4x5161 | RW | GIO 5 function | 0 | 255 | | See GIO function values above | |
| 3.0-> | 4x5162 | RW | SET Relay 1 function | | | | See SET Relay function values above | |
| 3.0-> | 4x5163 | RW | SET Relay 2 function | | | | See SET Relay function values above | |
| 3.1-> | 4x5173 | RW | GIO/SET DO POLARITY NO/NC | 0 | 255 | bit | BIT0=GIO1, BIT1=GIO2, BIT2=GIO3, BIT3=GIO4, BIT5=GIO5, BIT6=SET1DO, BIT7=SET2DO (0=Normally open, 1=Normally closed) | |
| 3.1-> | 4x5172 | RW | AO4 Output type | 0 | 4 | | 0=NA, 1=Control, 2=Stepless Control, 3=Temp SP, 4=Modbus | Available only if Room temperature control selected |

## GIO Modbus Control

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 4x5021 | RW | GIO1 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO1 Type Relay Output and Function Modbus (4x5157=143) |
| 3.0-> | 4x5022 | RW | GIO2 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO2 Type Relay Output and Function Modbus (4x5158=143) |
| 3.0-> | 4x5023 | RW | GIO3 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO3 Type Relay Output and Function Modbus (4x5159=143) |
| 3.0-> | 4x5024 | RW | GIO4 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO4 Type Relay Output and Function Modbus (4x5160=143) |
| 3.0-> | 4x5025 | RW | GIO5 Relay output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select IO5 Type Relay Output and Function Modbus (4x5161=143) |
| 3.0-> | 3x6349 | R | GIO 1 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO1 to Modbus input (4x5157=18) |
| 3.0-> | 3x6350 | R | GIO 2 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO2 to Modbus input (4x5158=18) |
| 3.0-> | 3x6351 | R | GIO 3 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO3 to Modbus input (4x5159=18) |
| 3.0-> | 3x6352 | R | GIO 4 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO4 to Modbus input (4x5160=18) |
| 3.0-> | 3x6353 | R | GIO 5 DI status | 0 | 1 | | 0=Open, 1=Closed | Select IO5 to Modbus input (4x5160=18) |
| 3.0-> | 3x6354 | R | GIO 1 AI value | 0 | 10000 | mV | Analog input voltage | Select IO1 to Modbus meas. (4x5157=66) |
| 3.0-> | 3x6355 | R | GIO 2 AI value | 0 | 10000 | mV | Analog input voltage | Select IO2 to Modbus meas. (4x5158=66) |
| 3.0-> | 3x6356 | R | GIO 3 AI value | 0 | 10000 | mV | Analog input voltage | Select IO3 to Modbus meas. (4x5159=66) |
| 3.0-> | 3x6357 | R | GIO 4 AI value | 0 | 10000 | mV | Analog input voltage | Select IO4 to Modbus meas. (4x5160=66) |
| 3.0-> | 3x6358 | R | GIO 5 AI value | 0 | 10000 | mV | Analog input voltage | Select IO5 to Modbus meas. (4x5161=66) |
| 3.0-> | 4x5026 | RW | SET Relay 1 output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select SET Relay 1 to Modbus (4x5162=15) |
| 3.0-> | 4x5027 | RW | SET Relay 2 output | 0 | 1 | | 0=External Relay Open, 1=External Relay Closed | Select SET Relay 2 to Modbus (4x5163=15) |
| 3.0-> | 4x5028 | RW | AO4 Output control | 0 | 1000 | 0.01V | AO4 Voltage output control | Select AO4 Function to Modbus (4x5172=4) |

## Measurement Inputs

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 4.0-> | 4x5131 | RW | Room Temperature sensor used for functions | 0 | | | 0=Internal Extract sensor temperature/sensors package, 1=T6, 2=T7, 3=T7, 4=T9, 5=GIO1, 6=GIO2, 7=GIO3, 8=GIO4, 9=GIO5, 10=User Panel 1, 11=UP2, 12=UP3, 13=UP4, 14=UP5 | Note: when room temperature sensor is selected make sure that sensor measurement exists and is correct. Used for summer mode selection, summer night boost or room temperature control |
| 4.0-> | 4x5190 | RW | T6 External Room Temperature Sensor type | 0 | 1 | | 0=Swegon PTC, 1=PT1000. Temperature can be read from 3x6278 | SET Sensor inputs can be used as room temperature sensor if T6 is not reserved for water freezing protection sensor |
| 4.0-> | 4x5191 | RW | T7 External Room Temperature Sensor type | 0 | 1 | | 0=Swegon PTC, 1=PT1000. Temperature can be read from 3x6279 | SET Sensor inputs can be used as room temperature sensor if T7 is not reserved for supply temperature sensor |
| 4.0-> | 4x5192 | RW | T8 External Room Temperature Sensor type | 0 | 1 | | 0=Swegon PTC, 1=PT1000. Temperature can be read from 3x6280 | SET Sensor inputs can be used as room temperature sensor if T8 is not reserved for external outside temperature sensor |
| 4.0-> | 4x5193 | RW | T9 External Room Temperature Sensor type | 0 | 1 | | 0=Swegon PTC, 1=PT1000. Temperature can be read from 3x6281 | SET Sensor inputs can be used as room temperature sensor if T9 is not reserved for external heating circuit sensor |
| 4.0-> | 4x5194 | RW | GIO Temp measurement scale input low | 0 | 10000 | mV | 0-10V measurement scaling values | |
| 4.0-> | 4x5195 | RW | GIO Temp measurement scale input high | 0 | 10000 | mV | 0-10V measurement scaling values | |
| 4.0-> | 4x5196 | RW | GIO Temp measurement scale Temp output low | -500 | 500 | 0.1°C | AI (0-10V) measurement scaling values | |
| 4.0-> | 4x5197 | RW | GIO Temp measurement scale Temp output high | -500 | 500 | 0.1°C | 0-10V measurement scaling values | |
| 4.0-> | 4x5132 | RW | Room Temperature Fine Tuning | -100 | 100 | 0.1°C | Room Temperature Fine tuning | |
| 4.0-> | 4x5151 | RW | T8 External Outside Temperature Sensor | 0 | 2 | | 0=Internal fresh air sensor, 1=T8 External Swegon PTC, 2=T8 External PT1000 | If accurate outside temperature measurement is required, external outside temperature sensor can be installed to T8 sensor input |
| 4.0-> | 4x5209 | RW | RH measurement | 0 | 5 | | 0=IO1, 1=IO2, 2=IO3, 3=IO4, 4=IO5, 5=Internal sensor, 6=Average, 7=Highest, 8=Lowest | |
| 4.0-> | 4x5210 | RW | GIO RH measurement scale input low | 0 | 10000 | mV | 0-10V measurement scaling values | |
| 4.0-> | 4x5211 | RW | GIO RH measurement scale input high | 0 | 10000 | mV | | |
| 4.0-> | 4x5212 | RW | GIO RH measurement scale rh output low | 0 | 100 | % | | |
| 4.0-> | 4x5213 | RW | GIO RH measurement scale rh output high | 0 | 100 | % | | |
| 4.0-> | 4x5214 | RW | CO2 measurement | 0 | 5 | | 0=IO1, 1=IO2, 2=IO3, 3=IO4, 4=IO5, 5=Internal sensor, 6=Average, 7=Highest, 8=Lowest | |
| 4.0-> | 4x5215 | RW | GIO CO2 measurement scale input low | 0 | 10000 | mV | 0-10V measurement scaling values | |
| 4.0-> | 4x5216 | RW | GIO CO2 measurement scale input high | 0 | 10000 | mV | | |
| 4.0-> | 4x5217 | RW | GIO CO2 measurement scale CO2 output low | 0 | 5000 | ppm | | |
| 4.0-> | 4x5218 | RW | GIO CO2 measurement scale CO2 output high | 0 | 5000 | ppm | | |
| 4.0-> | 4x5219 | RW | VOC measurement | 0 | 5 | | 0=IO1, 1=IO2, 2=IO3, 3=IO4, 4=IO5, 5=Internal sensor, 6=Average, 7=Highest, 8=Lowest | |
| 4.0-> | 4x5220 | RW | GIO VOC measurement scale input low | 0 | 10000 | mV | 0-10V measurement scaling values | |
| 4.0-> | 4x5221 | RW | GIO VOC measurement scale input high | 0 | 10000 | mV | | |
| 4.0-> | 4x5222 | RW | GIO VOC measurement scale VOC output low | 0 | 5000 | ppm | | |
| 4.0-> | 4x5223 | RW | GIO VOC measurement scale VOC output high | 0 | 5000 | ppm | | |

## Airflow Adjustment

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 4x5029 | RW | Commissioning Mode | 0 | 9 | | 0=Not in use, 1=Away, 2=Home, 3=Boost, 4=Cooking mode, 5=End | |
| 3.0-> | 4x5302 | RW | Away mode Supply fan speed | 20 | Home | % | fan speed | Don't use this register for external fan control |
| 3.0-> | 4x5303 | RW | Away mode Exhaust fan speed | 20 | Home | % | fan speed | Don't use this register for external fan control |
| 3.0-> | 4x5304 | RW | Home mode Supply fan speed | Away | Boost | % | fan speed | Don't use this register for external fan control |
| 3.0-> | 4x5305 | RW | Home mode Exhaust fan speed | Away | Boost | % | fan speed | Don't use this register for external fan control |
| 3.0-> | 4x5306 | RW | Boost mode Supply fan speed | Home | 100 | % | fan speed | Don't use this register for external fan control |
| 3.0-> | 4x5307 | RW | Boost mode Exhaust fan speed | Home | 100 | % | fan speed | Don't use this register for external fan control |
| 4.0-> | 4x5020 | RW | Cooker Hood mode | 0 | 4 | | 0=Not Selected, 1=Hood connected to ventilation unit, 2=Roof fan, 3=Integrated fan, 4=Recirculating cooker hood | Note: when cookerhood mode 2-4 is selected the ventilation unit can not be controlled with cooker hood |
| 4.0-> | 4x5184 | RW | Cooking mode Supply fan speed | 20 | 100 | % | Cooking mode fan control | Note: select cooking mode before adjustment |
| 4.0-> | 4x5185 | RW | Cooking mode Exhaust fan speed | 20 | 100 | % | Cooking mode fan control | Note: select cooking mode before adjustment |
| 3.0-> | 4x5318 | RW | Ventilation control mode | 0 | 5 | | 0=Normal, 1=PA Supply control, 2=PA Extract control, 3=PA control, 4=l/s control | If PA or l/s control is selected, commissioning must be done with User Panel |
| 3.0-> | 4x5312 | RW | Away mode Supply Pressure | 0 | 255 | PA | Ventilation Pressure | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0-> | 4x5313 | RW | Away mode Exhaust Pressure | 0 | 255 | PA | Ventilation Pressure | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0-> | 4x5314 | RW | Home mode Supply Pressure | 0 | 255 | PA | Ventilation Pressure | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0-> | 4x5315 | RW | Home mode Exhaust Pressure | 0 | 255 | PA | Ventilation Pressure | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0-> | 4x5316 | RW | Boost mode Supply Pressure | 0 | 255 | PA | Ventilation Pressure | Commissioning must be done with User Panel in Commissioning Mode |
| 3.0-> | 4x5317 | RW | Boost mode Exhaust Pressure | 0 | 255 | PA | Ventilation Pressure | Commissioning must be done with User Panel in Commissioning Mode |

## Alarms

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 4x5141 | RW | Service Reminder | 0 | 1 | | 0=Disabled, 1=Enabled | Service time can be reset by writing 0 and then 1 to this register |
| 3.0-> | 3x6343 | R | Hours to next Service | 0 | 10000 | Hours | | Available if Service Reminder enabled (see 4x5142 for Service Interval) |
| 3.0-> | 4x5142 | RW | Service Reminder interval | 0 | 12 | months | | |
| 3.0-> | 3x6129 | R | Service Info | 0 | 1 | | 0=No Alarms, 1=Unconfirmed Info Alarm | 3x6136 Bit 9 |
| 3.0-> | 4x5406 | W | Reset All info alarms | 0 | 1 | | 1=Confirm Alarm, Register is cleared when command is processed | |
| 4.0-> | 3x6195 | R | Critical Alarms (Ventilation stopped) | 0 | 1 | | 0=No Alarms, 1=Critical Alarm | Only in Genius control system |
| 3.0-> | 3x6132 | R | Active Alarms | 0 | 1 | | 0=No Alarms, 1=Active Alarm | |
| 3.0-> | 3x6133 | R | Unconfirmed Info | 0 | 1 | | 0=No Unconfirmed alarms, 1=Unconfirmed alarms | |
| 3.0-> | 3x6136 | R | Active Alarms Bitwise - 1 | 0 | 16bit | | 0=No Alarm, 1=Active alarm. See bit information below | |
| 3.0-> | 3x6137 | R | Resettable alarm bitwise - 1 (Past active alarm) | 0 | 16bit | | 0=No past alarm, 1=Past active alarm. See bit information below | |
| 3.0-> | 3x6117 / 3x6118 | R | E011 Postheater failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 0 / 3x6137 Bit 0 (0000 0000 0000 0001) |
| 3.0-> | 3x6119 / 3x6120 | R | E021 Preheater failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 1 / 3x6137 Bit 1 |
| 3.0-> | Reserved | | | | | | | 3x6136 Bit 2 / 3x6137 Bit 2 |
| 3.0-> | 3x6121 / 3x6122 | R | E041 Freezing danger / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 3 / 3x6137 Bit 3 |
| 3.0-> | 3x6125 / 3x6126 | R | E051 Supply Fan Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 4 / 3x6137 Bit 4 |
| 3.0-> | 3x6127 / 3x6128 | R | E061 Exhaust Fan Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 5 / 3x6137 Bit 5 |
| 3.0-> | 3x6101 / 3x6109 | R | E151/E161 T1 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6102 / 3x6110 | R | E152/E162 T2 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6103 / 3x6112 | R | E153/E163 T3 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6104 / 3x6113 | R | E154/E164 T4 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6105 / 3x6114 | R | E155/E165 T5 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6106 / 3x6115 | R | E156/E166 T6 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6107 / 3x6116 | R | E157/E167 T7 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6108 / 3x6117 | R | E158/E168 T8 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6134 / 3x6135 | R | E159/E169 T9 Temperature Sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 6 / 3x6137 Bit 6 |
| 3.0-> | 3x6131 | R | E071 Emergency Stop | 0 | 1 | | 0=No Alarms, 1=Active Alarm | 3x6136 Bit 7 |
| 3.0-> | 3x6130 | R | Reserved | 0 | 1 | | | 3x6317 Bit 8 |
| 3.0-> | 3x6129 | R | Service Info | 0 | 1 | | 0=No Alarms, 1=Service info | 3x6137 Bit 9 |
| 3.0-> | 3x6123 / 3x6124 | R | New Genius alarm / Genius unconfirmed alarm | 0 | 1 | | 0=No Genius alarms, 1=Active Genius alarm / Resettable alarm | 3x6136 Bit 10 / 3x6137 Bit 10 |
| 3.0-> | 3x6143 / 3x6144 | R | E111 Supply temperature low alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 11 / 3x6137 Bit 11 |
| 3.0-> | 3x6145 / 3x6146 | R | E121 Internal temperature high alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 12 / 3x6137 Bit 12 |
| 3.0-> | 3x6141 / 3x6142 | R | Preheater temperature high alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 13 / 3x6137 Bit 13 |
| 3.1-> | 3x6147 / 3x6148 | R | E131 Rotor RPM alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 14 / 3x6137 Bit 14 |
| 3.0-> | 3x6149 / 3x6150 | R | Fan Control alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6136 Bit 15 / 3x6137 Bit 15 (1000 0000 0000 0000) |

## Genius Control System New Alarms

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 4.0-> | 3x6191 | R | Active Alarms Bitwise - 2 | 0 | 16bit | | 0=No Alarm, 1=Active alarm. See bit information below | |
| 4.0-> | 3x6192 | R | Resettable Alarms Bitwise - 2 (Active alarm in the past) | 0 | 16bit | | 0=No info, 1=Unconfirmed Info alarm. See bit information below | |
| 4.0-> | 3x6151 / 3x6152 | R | E171 Sensor package Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 0 / 3x6192 Bit 0 (0000 0000 0000 0001) |
| 4.0-> | 3x6153 / 3x6154 | R | E172 RH sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 1 / 3x6192 Bit 1 |
| 4.0-> | 3x6155 / 3x6156 | R | E173 CO2 sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 2 / 3x6192 Bit 2 |
| 4.0-> | 3x6157 / 3x6158 | R | E174 VOC sensor Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 3 / 3x6192 Bit 3 |
| 4.0-> | 3x6159 / 3x6160 | R | E031 External Electrical Preheater Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 4 / 3x6192 Bit 4 |
| 4.0-> | 3x6161 / 3x6162 | R | E181 External Electrical Postheater Failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 5 / 3x6192 Bit 5 |
| 4.0-> | 3x6163 / 3x6164 | R | E071 Internal PCB Temperature High / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 6 / 3x6192 Bit 6 |
| 4.0-> | 3x6165 / 3x6166 | R | Internal Parameter error / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 7 / 3x6192 Bit 7 |
| 4.0-> | 3x6167 / 3x6168 | R | E091 External Alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 8 / 3x6192 Bit 8 |
| 4.0-> | 3x6169 / 3x6170 | R | E093 External device message / Resettable message | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 9 / 3x6192 Bit 9 |
| 4.0-> | 3x6171 / 3x6172 | R | E092 External critical alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 10 / 3x6192 Bit 10 |
| 4.0-> | 3x6173 / 3x6174 | R | E101 External Fire detector alarm / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 11 / 3x6192 Bit 11 |
| 4.0-> | 3x6175 / 3x6176 | R | E141 Heat exchanger efficiency low / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 12 / 3x6192 Bit 12 |
| 4.0-> | 3x6177 / 3x6178 | R | Heat exchanger control failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6191 Bit 13 / 3x6192 Bit 13 (0010 0000 0000 0000) |
| 4.0-> | 3x6193 | R | Active Alarms Bitwise - 3 | 0 | 16bit | | 0=No Alarm, 1=Active alarm. See bit information below | |
| 4.0-> | 3x6194 | R | Unconfirmed Alarms Bitwise - 3 (Active alarm in the past) | 0 | 16bit | | 0=No info, 1=Unconfirmed Info alarm. See bit information below | |
| 4.0-> | 3x6179 / 3x6180 | R | E191 Cooling condenser temperature high / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 0 / 3x6194 Bit 0 (0000 0000 0000 0001) |
| 4.0-> | 3x6181 / 3x6182 | R | E192 Cooling hotgas temperature high / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 1 / 3x6194 Bit 1 |
| 4.0-> | 3x6183 / 3x6184 | R | E193 Cooling pressure high / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 2 / 3x6194 Bit 2 |
| 4.0-> | 3x6185 / 3x6186 | R | E134 Rotor stall detection / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 3 / 3x6194 Bit 3 |
| 4.0-> | 3x6187 / 3x6188 | R | E133 Rotor driver overheat / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 4 / 3x6194 Bit 4 |
| 4.0-> | 3x6189 / 3x6190 | R | E132 Rotor connection failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 5 / 3x6194 Bit 5 |
| 4.1-> | 3x6196 / 3x6197 | R | E502 Indoor humidity / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 6 / 3x6194 Bit 6 |
| 4.1-> | 3x6198 / 3x6199 | R | E512 Cooling coil condense removal critical failure / Resettable alarm | 0 | 1 | | 0=Not active alarm, 1=Active / Resettable alarm | 3x6193 Bit 7 / 3x6194 Bit 7 |

## Device Information

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 3x6001 | R | Device Firmware version major | 0 | 99 | | | |
| 3.0-> | 3x6002 | R | Device Firmware version minor | 0 | 99 | | | |
| 3.0-> | 3x6003 | R | Device Firmware build | 0 | 999 | | | |
| 3.0-> | 3x6004 | R | Parameter build | 0 | 99 | | | |
| 3.0-> | 3x6005 | R | Parameter minor build | 0 | 99 | | | |
| 3.0-> | 3x6008 | R | Model name[0:14] | | | ASCII | Model name ASCII code | 3x16008 - 3x16024 |
| 3.0-> | 3x6024 | R | Unit Serial Number[0:23] | | | ASCII | Unit serial number ASCII code | 3x6024 - 3x6047, Direct Access to Service Portal |

## Diagnostics - Measurements

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 3x6201 | R | Fresh air temperature | -550 | 600 | 0.1°C | Ventilation unit internal outside air temperature (Filtered) | T1 sensor |
| 3.0-> | 3x6202 | R | Supply air before re-heater temperature | -550 | 600 | 0.1°C | Heat exchanger supply temperature T2 or calculated from supply temperature T4 by scaling internal postheater effect | |
| 3.0-> | 3x6203 | R | Supply air temperature | -550 | 600 | 0.1°C | Effective supply air temperature. If external heater/cooling devices are installed external sensor is used | T4 or T7 if external sensor is installed |
| 3.0-> | 3x6204 | R | Extract air temperature | -550 | 600 | 0.1°C | Extract air/Air from the room temperature | T3 or Sensor package |
| 3.0-> | 3x6205 | R | Exhaust air temperature | -550 | 600 | 0.1°C | Exhaust/Waste air temperature | T5 if sensor installed to unit |
| 3.0-> | 3x6209 | R | Water Radiator temperature | -550 | 600 | 0.1°C | Water battery freezing protection measurement | T6 if with water based radiator installed |
| 3.0-> | 3x6211 | R | External Outside air temperature | -550 | 600 | 0.1°C | External outside temperature | T8 if External PreHeater/Cooling control or if external outside sensor measurement is selected |
| 3.0-> | 3x6206 | R | Room air temperature | -550 | 600 | 0.1°C | Effective room air temperature, sensor defined with register | |
| 4.0-> | 3x6278 | R | T6 room temperature | -550 | 600 | 0.1°C | External room temperature sensor, type (PTC/PT1000) defined with register 4x1407 | |
| 4.0-> | 3x6279 | R | T7 room temperature | -550 | 600 | 0.1°C | External room temperature sensor, type (PTC/PT1000) defined with register 4x1408 | |
| 4.0-> | 3x6280 | R | T8 room temperature | -550 | 600 | 0.1°C | External room temperature sensor, type (PTC/PT1000) defined with register 4x1409 | |
| 4.0-> | 3x6281 | R | T9 room temperature | -550 | 600 | 0.1°C | External room temperature sensor, type (PTC/PT1000) defined with register 4x1410 | |
| 4.0-> | 3x6282 / 3x6207 | R | User Panel 1 temperature | -550 | 600 | 0.1°C | User panel internal temperature measurement | |
| 4.0-> | 3x6283 / 3x6208 | R | User Panel 2 temperature | -550 | 600 | 0.1°C | User panel internal temperature measurement | |
| 4.0-> | 3x6284 | R | User Panel 3 temperature | -550 | 600 | 0.1°C | User panel internal temperature measurement | |
| 4.0-> | 3x6285 | R | User Panel 4 temperature | -550 | 600 | 0.1°C | User panel internal temperature measurement | |
| 4.0-> | 3x6286 | R | User Panel 5 temperature | -550 | 600 | 0.1°C | User panel internal temperature measurement | |
| 4.0-> | 3x6287 | R | IO1 temperature | -550 | 600 | 0.1°C | 0-10V temperature transmitter connected to IO1 | |
| 4.0-> | 3x6288 | R | IO2 temperature | -550 | 600 | 0.1°C | 0-10V temperature transmitter connected to IO2 | |
| 4.0-> | 3x6289 | R | IO3 temperature | -550 | 600 | 0.1°C | 0-10V temperature transmitter connected to IO3 | |
| 4.0-> | 3x6290 | R | IO4 temperature | -550 | 600 | 0.1°C | 0-10V temperature transmitter connected to IO4 | |
| 4.0-> | 3x6291 | R | IO5 temperature | -550 | 600 | 0.1°C | 0-10V temperature transmitter connected to IO5 | |
| 3.0-> | 3x6213 | R | Room air CO2 | 450 | 2000 | ppm | Effective CO2 measurement, define used sensor with register 4x5214 | Filtered CO2 value |
| 4.0-> | 3x6263 | R | CO2 internal sensor | 450 | 2000 | ppm | Ventilation unit internal sensor | |
| 4.0-> | 3x6258 | R | CO2 IO1 | 0 | 5000 | ppm | External CO2 sensor connected to IO1 | |
| 4.0-> | 3x6259 | R | CO2 IO2 | 0 | 5000 | ppm | External CO2 sensor connected to IO2 | |
| 4.0-> | 3x6260 | R | CO2 IO3 | 0 | 5000 | ppm | External CO2 sensor connected to IO3 | |
| 4.0-> | 3x6261 | R | CO2 IO4 | 0 | 5000 | ppm | External CO2 sensor connected to IO4 | |
| 4.0-> | 3x6262 | R | CO2 IO5 | 0 | 5000 | ppm | External CO2 sensor connected to IO5 | |
| 3.0-> | 3x6214 | R | Room air RH (%) | 0 | 100 | % | Effective RH measurement, define used sensor with register 4x5209 | |
| 4.0-> | 3x6215 | R | Room air AH (g/m3) | 0 | 5000 | 0.01g/m3 | Calculated absolute humidity, used in RH automation function | |
| 4.0-> | 3x6216 | R | Room air AH SetPoint (g/m3) | 0 | 5000 | 0.01g/m3 | Calculated absolute humidity boost limit, used in RH automation function | |
| 4.0-> | 3x6269 | R | RH internal sensor | 450 | 2000 | % | Ventilation unit internal sensor | |
| 4.0-> | 3x6264 | R | RH IO1 | 0 | 5000 | % | External RH sensor connected to IO1 | |
| 4.0-> | 3x6265 | R | RH IO2 | 0 | 5000 | % | External RH sensor connected to IO2 | |
| 4.0-> | 3x6266 | R | RH IO3 | 0 | 5000 | % | External RH sensor connected to IO3 | |
| 4.0-> | 3x6267 | R | RH IO4 | 0 | 5000 | % | External RH sensor connected to IO4 | |
| 4.0-> | 3x6268 | R | RH IO5 | 0 | 5000 | % | External RH sensor connected to IO5 | |
| 3.0-> | 3x6217 | R | Room air VOC | 0 | 2000 | ppm | Effective VOC measurement, define used sensor with register 4x5219 | Available only in units with VOC sensor |
| 4.0-> | 3x6275 | R | VOC internal sensor | 450 | 2000 | ppm | Ventilation unit internal sensor | |
| 4.0-> | 3x6270 | R | VOC IO1 | 0 | 5000 | ppm | External VOC sensor connected to IO1 | |
| 4.0-> | 3x6271 | R | VOC IO2 | 0 | 5000 | ppm | External VOC sensor connected to IO2 | |
| 4.0-> | 3x6272 | R | VOC IO3 | 0 | 5000 | ppm | External VOC sensor connected to IO3 | |
| 4.0-> | 3x6273 | R | VOC IO4 | 0 | 5000 | ppm | External VOC sensor connected to IO4 | |
| 4.0-> | 3x6274 | R | VOC IO5 | 0 | 5000 | ppm | External VOC sensor connected to IO5 | |
| 3.0-> | 3x6218 | R | Supply Duct Pressure | 0 | 500 | Pa | | External duct pressure sensor is needed |
| 3.0-> | 3x6219 | R | Exhaust Duct Pressure | 0 | 500 | Pa | | External duct pressure sensor is needed |
| 3.0-> | 3x6220 | R | Supply Air Flow | 0 | 500 | l/s | | External Air flow sensor is needed and K value needs to be adjusted |
| 3.0-> | 3x6221 | R | Exhaust Air Flow | 0 | 500 | l/s | | External Air flow sensor is needed and K value needs to be adjusted |
| 4.0-> | 3x6277 | R | Room pressure | -500 | 500 | 0.1Pa | External measurement of building out/in pressure difference | |

## Diagnostics - Unit Status

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 3.0-> | 3x6301 | R | Unit state | 0 | 4 | | 0=Critical Stop, 1=User Stopped, 2=Starting, 3=Normal, 4=Commissioning | |
| 3.0-> | 3x6308 | R | Boost Time left | 0 | 120 | min | Timed Function remaining time | |
| 3.0-> | 3x6309 | R | Week Timer Active | 0 | 10 | | 0=Weekly timer not Active, 1=Stopped, 2=Travelling, 3=Away, 4=Silent, 5=Home, 6=Home+, 7=Boost, 8=NA, 9=NA, 10=Weekly timer interrupted | |
| 3.0-> | 3x6307 | R | Travelling mode Active | 0 | 1 | | 0=Function Not Active, 1=Travelling mode active | |
| 4.0-> | 3x6325 | R | Silent mode Active | 0 | 1 | | 0=Function Not Active, 1=Silent mode active, no boosting allowed | |
| 3.0-> | 3x6335 | R | Fireplace function active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0-> | 3x6336 | R | Central Vacuum Cleaner function active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0-> | 3x6337 | R | Cooking mode Active | 0 | 1 | | 0=Function Not Active, 1=Function Active | |
| 3.0-> | 3x6302 | R | Ventilation Speed state (compatibility to Smart) | 0 | 4 | | 0=Stopped, 1=Away, 2=Home, 3=Boost | |
| 4.0-> | 3x6434 | R | Ventilation Speed state (Genius) | 0 | 4 | | 0=Stopped, 1=Travelling, 2=Away, 3=Home, 4=Home+, 5=Boost, 6=Fireplace | |
| 3.0-> | 3x6303 | R | Supply Fan Control | 0 | 100 | % | | |
| 3.0-> | 3x6304 | R | Exhaust Fan Control | 0 | 100 | % | | |
| 3.0-> | 3x6305 | R | Supply Fan RPM | 0 | 5000 | 1/min | | Fan RPM measurement is needed |
| 3.0-> | 3x6306 | R | Exhaust Fan RPM | 0 | 5000 | 1/min | | Fan RPM measurement is needed |
| 3.0-> | 3x6315 | R | Automation control +/- of Home mode | -100 | 100 | % | Ventilation is controlled steplessly from selected mode according to this register | |
| 3.0-> | 3x6310 | R | CO2 Automation | -100 | 100 | % | Fan control change based on CO2 automation | Available only in units with CO2 sensor |
| 3.0-> | 3x6311 | R | RH Automation | 0 | 100 | % | Fan control boost based on RH automation | Available only in units with RH sensor |
| 3.0-> | 3x6312 | R | VOC Automation | 0 | 100 | % | Fan control boost based on VOC automation | Available only in units with VOC sensor |
| 3.0-> | 3x6313 | R | Temperature boost | 0 | 100 | % | Fan control boost based on summer mode boost | |
| 3.0-> | 3x6314 | R | Fan Speed limit Control (Supply temperature low, ventilation reduction) | -100 | 0 | % | Fan control change based on cold climate control. Note: depending on unit model fan control change method may vary | |
| 4.0-> | 3x6382 | R | Building pressure balance control | -50 | 50 | % | Building pressure control, negative value decreases extract airflow and positive increases the airflow | External room pressure sensor is needed |
| 4.0-> | 3x6370 | R | Heating state | | | | 0=Starting, 1=Stopped, 2=External Cooling, 3=Internal Cooling, 4=Internal Cooling limited, 5=Summer mode control, 6=Heat exchanger control, 7=Heating, 8=Defrost 1, 9=Defrost 2, 10=Defrost 3 | |
| 4.0-> | 3x6320 | R | Temperature Setpoint | 13 | 25 | °C | Effective supply temperature setpoint, controlled either by user setpoint, summer mode, away or travelling mode or by room temperature controller | Available only in units with controlled re-heater |
| 4.0-> | 3x6317 | R | Combined Post heating external/internal control | 0 | 100 | % | Internal postheating 0-100%, External Postheating 0-200% | |
| 4.0-> | 3x6318 | R | Internal post heating control | 0 | 100 | % | Internal electrical postheater control. Power (W) depends on post heater power | Available only in units with internal postheater |
| 4.0-> | 3x6344 | R | Internal Preheater control | 0 | 100 | % | Internal electrical preheater control. Power (W) depends on preheater power | Available only in units with Preheater |
| 4.0-> | 3x6319 | R | External post heating control water | 0 | 100 | % | External heating coil control (valve position). 100% equals 10V control signal | Available only in units with external postheater |
| 4.0-> | 3x6322 | R | External post heating control electrical | 0 | 100 | % | External heating coil control (power control). 100% equals 10V control signal | Available only in units with external postheater |
| 4.0-> | 3x6321 | R | External post cooling control | 0 | 100 | % | External cooling control (valve position). 100% equals 10V control signal | Available only in units with external post cooler |
| 3.0-> | 3x6323 | R | External post cooling active | 0 | 1 | | External cooling control active | Available only in units with external post cooler |
| 4.0-> | 3x6345 | R | External Preheater control | 0 | 100 | % | External preheater control. Power (W) depends on preheater power | |
| 4.0-> | 3x6331 | R | External preheater/cooling output | 0 | 1 | | 0=Not active, 1=Active, 2=Idle for pump/valve anti jamming | |
| 4.0-> | 3x6348 | R | Heat exchanger bypass plate position | 0 | 100 | % | Bypass plate: 100%=full open, 0%=Closed | |
| 4.0-> | 3x6332 | R | Rotor control | 0 | 1000 | 0.1% | % of max speed with 1 decimal accuracy | |
| 4.0-> | 3x6234 | R | Rotor rotating speed | 0 | 2000 | 0.1/min | Rotation speed 0.1 rotations / minute | |

## Room Controllers

Controller Type values: 0=LUNA d MB, 1=Produal TRC-1A2T-MOD-24-W, 2=Produal CU-LH (1), 3=Produal CU-LH (2)

Controller Location values: 0=Controller disabled, 1=Living room 1, 2=Living room 2, 3=Living room 3, 4=Bedroom 1, 5=Bedroom 2, 6=Bedroom 3, 7=Bedroom 4, 8=Bedroom 5, 9=Hallway, 10=Kitchen, 11=Dining room, 12=Bathroom, 13=Utility room, 14=Walk-in closet, 15=Storage room, 16=Garage, 17=Technical room, 18=Zone 1, 19=Zone 2, 20=Zone 3, 21=Zone 4

| SW | Register | R/W | Register Name | Min | Max | Unit | Description | Note |
|---|---|---|---|---|---|---|---|---|
| 4.1-> | 4x1505 | RW | Controller 1 ID | 6 | 247 | | Configure room controllers with individual IDs | |
| 4.1-> | 4x1506 | RW | Controller 2 ID | 6 | 247 | | | |
| 4.1-> | 4x1507 | RW | Controller 3 ID | 6 | 247 | | | |
| 4.1-> | 4x1508 | RW | Controller 4 ID | 6 | 247 | | | |
| 4.1-> | 4x1509 | RW | Controller 5 ID | 6 | 247 | | | |
| 4.1-> | 4x1510 | RW | Controller 6 ID | 6 | 247 | | | |
| 4.1-> | 4x1511 | RW | Controller 7 ID | 6 | 247 | | | |
| 4.1-> | 4x1512 | RW | Controller 1 Type | 0 | 3 | | See Controller Type values above | |
| 4.1-> | 4x1513 | RW | Controller 2 Type | 0 | 3 | | | |
| 4.1-> | 4x1514 | RW | Controller 3 Type | 0 | 3 | | | |
| 4.1-> | 4x1515 | RW | Controller 4 Type | 0 | 3 | | | |
| 4.1-> | 4x1516 | RW | Controller 5 Type | 0 | 3 | | | |
| 4.1-> | 4x1517 | RW | Controller 6 Type | 0 | 3 | | | |
| 4.1-> | 4x1518 | RW | Controller 7 Type | 0 | 3 | | | |
| 4.1-> | 4x1519 | RW | Controller 1 Location | 0 | 21 | | See Controller Location values above | |
| 4.1-> | 4x1520 | RW | Controller 2 Location | 0 | 21 | | | |
| 4.1-> | 4x1521 | RW | Controller 3 Location | 0 | 21 | | | |
| 4.1-> | 4x1522 | RW | Controller 4 Location | 0 | 21 | | | |
| 4.1-> | 4x1523 | RW | Controller 5 Location | 0 | 21 | | | |
| 4.1-> | 4x1524 | RW | Controller 6 Location | 0 | 21 | | | |
| 4.1-> | 4x1525 | RW | Controller 7 Location | 0 | 21 | | | |
| 4.1-> | 4x1526 | RW | Controller 1 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | 0=Use controller knob setpoint, 1=Override setpoint defined with register 4x1542-4x1548 | LUNA d MB controller uses by default setpoint defined with the knob located on controller |
| 4.1-> | 4x1527 | RW | Controller 2 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | | |
| 4.1-> | 4x1528 | RW | Controller 3 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | | |
| 4.1-> | 4x1529 | RW | Controller 4 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | | |
| 4.1-> | 4x1530 | RW | Controller 5 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | | |
| 4.1-> | 4x1531 | RW | Controller 6 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | | |
| 4.1-> | 4x1532 | RW | Controller 7 Setpoint override (Only LUNA d MB controller) | 0 | 1 | | | |
| 4.1-> | 4x1542 | RW | Controller 1 Setpoint | 0 | 300 | 0.1°C | Room temperature setpoint | Only LUNA d MB controller |
| 4.1-> | 4x1543 | RW | Controller 2 Setpoint | 0 | 300 | 0.1°C | | |
| 4.1-> | 4x1544 | RW | Controller 3 Setpoint | 0 | 300 | 0.1°C | | |
| 4.1-> | 4x1545 | RW | Controller 4 Setpoint | 0 | 300 | 0.1°C | | |
| 4.1-> | 4x1546 | RW | Controller 5 Setpoint | 0 | 300 | 0.1°C | | |
| 4.1-> | 4x1547 | RW | Controller 6 Setpoint | 0 | 300 | 0.1°C | | |
| 4.1-> | 4x1548 | RW | Controller 7 Setpoint | 0 | 300 | 0.1°C | | |
| 4.1-> | 3x2253 | R | Controller 1 Room temperature | 0 | 300 | 0.1°C | Room temperature | |
| 4.1-> | 3x2254 | R | Controller 2 Room temperature | 0 | 300 | 0.1°C | | |
| 4.1-> | 3x2255 | R | Controller 3 Room temperature | 0 | 300 | 0.1°C | | |
| 4.1-> | 3x2256 | R | Controller 4 Room temperature | 0 | 300 | 0.1°C | | |
| 4.1-> | 3x2257 | R | Controller 5 Room temperature | 0 | 300 | 0.1°C | | |
| 4.1-> | 3x2258 | R | Controller 6 Room temperature | 0 | 300 | 0.1°C | | |
| 4.1-> | 3x2259 | R | Controller 7 Room temperature | 0 | 300 | 0.1°C | | |
