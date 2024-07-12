# Author : Arun CS
# Github : https://github.com/aruncs31s/

"""
Note That i've used Raspberry pi 2 b for this testing and when i try to connect DHT11 to GPIO4 and read it doesnt work but somehow by connecting the sensor to GPIO7 and passing 4 to the read_retry() function works

"""

import sys
import Adafruit_DHT


def temp():
    return Adafruit_DHT.read_retry(11, 4)[0]


def humidity():
    return Adafruit_DHT.read_retry(11, 4)[1]


temp()

if __name__ == "__main__":
    print(f"Temperature is {temp()} Humidity is {humidity()}")
