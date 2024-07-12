# Author : Arun CS
# Github : https://github.com/aruncs31s/
import sys
import Adafruit_DHT


def temp():
    print(Adafruit_DHT.read_retry(11, 4))


temp()
