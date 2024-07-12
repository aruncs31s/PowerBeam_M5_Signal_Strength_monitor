import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)


def rain_count():
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode("utf-8").strip()
                print(f"{data}")
    except KeyboardInterrupt:
        ser.close()
