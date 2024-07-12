from os import error
import serial
import time

rain_sensor = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)


def rain_count():
    try:
        while True:
            if rain_sensor.in_waiting > 0:
                data = rain_sensor.readline().decode("utf-8").strip()
                print(f"{data}")
                ser.close()
    except error as e:
        ser.close()
        print(e)
    finally:
        time.sleep(5)
        rain_count()
