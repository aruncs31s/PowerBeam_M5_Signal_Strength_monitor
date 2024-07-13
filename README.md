# PowerBeam_M5_Signal_Strength_monitor

<!--toc:start-->

- [PowerBeam_M5_Signal_Strength_monitor](#powerbeamm5signalstrengthmonitor)
  - [Python Dependencies](#python-dependencies) - [POC](#poc) - [Reading With Raspberry pi](#reading-with-raspberry-pi) - [Raspberry Pi Python Dependencies](#raspberry-pi-python-dependencies)
  <!--toc:end-->

This python script automates data retrieval (signal strength) from `Ubiquiti PowerBeam M5 400`` which uses `AirMax`
This Script has 3 parts

- Normal Reading
- Reading With Raspberry Pi

## Python Dependencies

```
requests
http
urllib3
```

### POC

![](image.png?raw=true)

### Implementation

- Configure PowerBeam M5
- Change the `base url` and passwords in the python code
- if error occurs google it or [contact me](https://github.com/aruncs31s/aruncs31s)

#### Reading With Raspberry pi

It reading with raspberry is more difficult and require these following for the temperature , humidity and rain sensing

1. DTH11 Sensor
2. Rain Sensor
   These are used for only to increase the accuracy

##### Raspberry Pi Python Dependencies

```
Adafruit_DHT
serial
```

also i have used interrupt to handle rain counting so this following code should be uploaded to `Arduino` or any other micro controller or SOC Boards like raspberry pi , i did not use the Raspberry pi because it does not have a software interrupt on the `2 B` model

```c
volatile int event_counter = 0;

// The interrupt service routine (ISR)
void countEvent() { event_counter++; }

void setup() {
  Serial.begin(9600);

  pinMode(2, INPUT_PULLUP); // Using internal pull-up resistor
  //I have also added 10KOhm Series With the meter

  // Attach the interrupt to pin 2 (interrupt 0), triggering on falling edge
  attachInterrupt(digitalPinToInterrupt(2), countEvent, FALLING);
}

void loop() {
Serial.println(event_counter);
delay(1000);
}
```
