#include "humid_temp_sensor.h"
void humidTempSensor::get_readings() {
  ht_sensor.measureHighPrecision(temperature, humidity);
}
void humidTempSensor::begin() {
  Wire.begin();
  ht_sensor.begin(Wire);
}