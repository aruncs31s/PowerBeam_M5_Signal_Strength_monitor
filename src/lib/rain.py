# Author : Arun CS
# Github : https://github.com/aruncs31s/


import serial

rain_sensor = serial.Serial("/dev/ttyAMA0", 9600, timeout=2)


def get_count():
    try:
        while True:
            if rain_sensor.in_waiting > 0:

                return int(rain_sensor.readline().decode("utf-8").strip())
                exit(0)
    except KeyboardInterrupt:
        rain_sensor.close()


def compare(rain_count_previous):
    if rain_count_previous == get_count():
        return True
    else:
        return False
