"""
* Author: ArunCS
* Github: https://github.com/aruncs31s/PowerBeam_M5_Signal_Strength_monitor
* Date: 2024-09-29

"""

import http.cookiejar as cookielib
import os
import time
from datetime import datetime

import requests
import urllib3

# To Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define URLs change the change_me in my case it was the default ip by the antena

# Get time and date
# For Sorting
date = datetime.now().strftime("%Y-%m-%d")

time_now = datetime.now().strftime("%H:%M:%S")

current_date = datetime.now().strftime("%Y-%m-%d")
# esp32/esp8266 web server link
esp_url = "http://192.168.67.50/data"
base_url = "https://172.16.36.13"
login_url = f"{base_url}/login.cgi"
status_url = f"{base_url}/status.cgi"

# Define headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Define login credentials
payload = {"username": "ubnt", "password": "c4s@admin", "uri": "/index.cgi"}

# Initialize session
session = requests.Session()

# Initialize a CookieJar to store cookies
session.cookies = cookielib.LWPCookieJar("cookies.txt")

# Get initial cookies from the login page
response = session.get(login_url, headers=headers, verify=False)
session.cookies.save()


response = session.post(login_url, data=payload, headers=headers, verify=False)
session.cookies.save()
#


# Function to get signal value , Change this data[][] to get desired values
def get_signal_value():
    response = session.get(status_url, headers=headers, verify=False)
    data = response.json()
    signal = data["wireless"]["signal"]
    return signal


def print_out(timestamp, signal_value):
    print(f"{timestamp} - Signal value: {signal_value} dBm ")


def get_esp_data():
    try:
        esp_response = requests.get(esp_url)
        data_json = esp_response.json()
        data = [
            data_json["temperature"],
            data_json["humidity"],
            data_json["battery_voltage"],
            data_json["light_sensor_value"],
        ]
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(0.01)
        get_esp_data()


def measure(date):
    output_file = f"readings/normal/{date}_log.txt"
    output_file_csv = f"readings/csv/{date}_log.csv"
    while True:
        try:
            timestamp = datetime.now().strftime("%H:%M:%S")
            data = get_esp_data()
            # Find if this is necceary
            time_now = datetime.now().strftime("%H:%M:%S")
            signal_value = get_signal_value()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"{time_now} - Signal value: {signal_value} dBm  Temp {data[0]} Humidity {data[1]} Battery Voltage {data[2]} Light {data[3]}\n"
            )
            # if int(datetime.now().strftime("%M")) % 5 == 0:
            # Save to file
            is_file_exists = os.path.isfile(output_file)
            with open(output_file, "a") as f:
                # Check if the file exists
                if not is_file_exists:
                    f.write(
                        "Time , Signal value , Temperature , Humidity , Battery Voltage , Light Sensor Value \n"
                    )
                f.write(
                    f"{timestamp} - Signal value: {signal_value} dBm  Temp {data[0]} Humidity {data[1]} Battery Voltage {data[2]} Light {data[3]}\n"
                )
            is_file_exists = os.path.isfile(output_file_csv)
            with open(output_file_csv, "a") as f:
                # Check if the file exists
                if not is_file_exists:
                    f.write(
                        "Time , Signal value , Temperature , Humidity , Battery Voltage , Light Sensor Value \n"
                    )
                f.write(
                    f"{time_now},{signal_value},{data[0]},{data[1]},{data[2]},{data[3]}\n"
                )
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
        new_date = datetime.now().strftime("%Y-%m-%d")
        if new_date != date:
            measure(new_date)


while True:
    try:
        measure(date)
    except Exception as e:
        print(f"An error occurred in the main loop: {e}")
        time.sleep(10)
        measure(date)
