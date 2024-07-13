from logging import error
import lib/rain
import humidity_temperature as dht
from datetime import datetime
import requests
import http.cookiejar as cookielib
import time
import urllib3
import serial

serial_port = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)


# To Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define URLs change the change_me in my case it was the default ip by the antena
base_url = "https://172.16.36.13"
login_url = f"{base_url}/login.cgi"
status_url = f"{base_url}/status.cgi"
output_file = "signal_log.txt"

# Define headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Define login credentials
payload = {"username": "ubnt", "password": "cs4@admin", "uri": "/index.cgi"}

# Initialize session
session = requests.Session()

# Initialize a CookieJar to store cookies
session.cookies = cookielib.LWPCookieJar("cookies.txt")

# Get initial cookies from the login page
response = session.get(login_url, headers=headers, verify=False)
session.cookies.save()


def login():
    response = session.post(login_url, data=payload, headers=headers, verify=False)
    session.cookies.save()


# Check if login was successful by checking cookies or a specific element in the response
login()
if "AIROS_F492BF4A5898" in session.cookies:
    print("Login successful")
else:
    print("Login failed")


# Function to get signal value , Change this data[][] to get desired values
def get_signal_value():
    response = session.get(status_url, headers=headers, verify=False)
    data = response.json()
    signal = data["wireless"]["signal"]
    return signal


rain_count_now = 0


def measure():
    while True:
        try:
            signal_value = get_signal_value()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"{timestamp} - Signal value: {signal_value} dBm , Rain_Count: {rain.get_count()} Humidity: {dht.humidity()} Rain Status: {rain.compare(rain_count_previous=rain_count_now)}"
            )
            # Save to file
            with open(output_file, "a") as f:
                f.write(f"{timestamp} - Signal value: {signal_value}\n")
            time.sleep(5)  # Adjust the delay as needed
            rain_count_now = rain.get_count()

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(10)  # Adjust the delay as needed


# Loop to repeatedly get the signal value
if __name__ == "__main__":
    while True:
        try:
            measure()
        except Exception as e:
            print(f"An error occurred in the main loop: {e}")
            login()
            time.sleep(10)  # Wait before restarting the loop
