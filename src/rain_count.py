import serial

rain_sensor = serial.Serial("/dev/ttyAMA0", 9600, timeout=2)


def count():
    try:
        while True:
            if rain_sensor.in_waiting > 0:
                data = rain_sensor.readline().decode("utf-8").strip()
                print(f"{data}")
                exit(0)
    except KeyboardInterrupt:
        rain_sensor.close()
