## Input Registers

| Register | Description          | Unit / Values                                                                                          |
|----------|----------------------|--------------------------------------------------------------------------------------------------------|
| 3x6201   | Fresh air temperature | 0.1 °C                                                                                                |
| 3x6203   | Supply air temperature | 0.1 °C                                                                                               |
| 3x6204   | Extract air temperature | 0.1 °C                                                                                              |
| 3x6213   | CO2                  | PPM                                                                                                    |
| 3x6214   | RH                   | %                                                                                                      |
| 3x6217   | VOC                  | PPM eqv.                                                                                               |
| 3x6205   | Supply fan RPM       | 1/s                                                                                                    |
| 3x6206   | Extract fan RPM      | 1/s                                                                                                    |
| 3x6301   | Unit state           | 0 = Ext. stop<br>1 = User stop<br>2 = Start<br>3 = Normal<br>4 = Commissioning                        |
| 3x6302   | Operating mode       | 0 = Stop<br>1 = Away<br>2 = Home<br>3 = Boost<br>4 = Travelling                                       |
| 3x6136   | Combined alarm       | See full list                                                                                          |
| 3x6137   | Combined info        | See full list                                                                                          |

## Holding Registers

| Register | Address | Description           | Unit / Values                                                              |
|----------|---------|-----------------------|----------------------------------------------------------------------------|
| 4x5001   | 38 400  | Operating mode        | 0 = Stop<br>1 = Away<br>2 = Home<br>3 = Boost<br>4 = Travelling           |
| 4x5018   | 38 400  | Emergency stop        | 0 = Disabled<br>1 = Active<br>2 = Overpressurising                        |
| 4x5101   |         | Temperature setpoint  | 0.1 °C                                                                     |
| 4x5406   |         | Reset all alarms      | 1 = Reset                                                                  |