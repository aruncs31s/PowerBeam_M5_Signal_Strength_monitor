import http.cookiejar as cookielib
import time
from datetime import datetime
from logging import error

import requests
import urllib3

# To Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define URLs change the change_me in my case it was the default ip by the antena

# Get time and date
date = datetime.now().strftime("%Y-%m-%d")

time_now = datetime.now().strftime("%H:%M:%S")

base_url = "https://172.16.36.13"
login_url = f"{base_url}/login.cgi"
status_url = f"{base_url}/status.cgi"
output_file = "signal_log.txt"
output_file_csv = f"readings/csv/{date}_log.csv"

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


# Function to get signal value , Change this data[][] to get desired values
def get_signal_value():
    response = session.get(status_url, headers=headers, verify=False)
    data = response.json()
    signal = data["wireless"]["signal"]
    return signal


def measure():
    while True:
        try:
            date = datetime.now().strftime("%Y-%m-%d")

            time_now = datetime.now().strftime("%H:%M:%S")

            signal_value = get_signal_value()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} - Signal value: {signal_value} dBm ")
            # Save to file
            with open(output_file, "a") as f:
                f.write(f"{timestamp} - Signal value: {signal_value} dBm   \n")
            with open(output_file_csv, "a") as f:
                f.write(f"{time_now},{signal_value}\n")
            time.sleep(300)
        except Exception as e:
            print(f"An error occurred: {e}")


#
# def measure():
#     global rain_count
#     while True:
#         try:
#             signal_value = get_signal_value()
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             print(f"{timestamp} - Signal value: {signal_value} dBm ")
#             # Save to file
#             with open(output_file, "a") as f:
#                 f.write(f"{timestamp} - Signal value: {signal_value} dBm \n")
#             time.sleep(5)
#         except Exception as e:
#             print(f"An error occurred: {e}")
#


while True:
    try:
        measure()
    except Exception as e:
        print(f"An error occurred in the main loop: {e}")
        time.sleep(1)
