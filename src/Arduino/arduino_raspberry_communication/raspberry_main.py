import serial
import time

try: 
    while True: 
        ser = serial.Serial('/dev/ttyAMA0' , 9600) 
        if ser.in_waiting> 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"{data}")
except KeyboardInterrupt:
    ser.close()
