from os import error
import serial
import time

rain_sensor = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)


def rain_count():
    try:
        if rain_sensor.in_waiting > 0:
            data = rain_sensor.readline().decode("utf-8").strip()
            print(f"{data}")
    except error as e:
        print(e)


rain_count()
