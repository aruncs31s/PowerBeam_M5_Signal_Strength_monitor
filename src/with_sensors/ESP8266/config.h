#ifndef __CONFIG_H_
#define __CONFIG_H_

#include <stdint.h> // Required for uint8_t

typedef struct Data {
  float light_sensor_value;
  float humidity;
  float temperature;
  float battery_voltage;
} Data;

#endif //!__CONFIG_H_
