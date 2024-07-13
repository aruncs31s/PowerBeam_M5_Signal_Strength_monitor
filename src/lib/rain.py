# Author : Arun CS
# Github : https://github.com/aruncs31s/


import serial

rain_sensor = serial.Serial("/dev/ttyAMA0", 9600, timeout=15)


def get_count():
    try:
        while True:
            if rain_sensor.in_waiting > 0:
                count = rain_sensor.readline().decode("utf-8").strip()
                rain_sensor.close()
                return int(count)
                exit(0)
    except KeyboardInterrupt:
        rain_sensor.close()


def compare(rain_count_previous):
    if int(rain_count_previous) == get_count():
        return False
    else:
        return True
