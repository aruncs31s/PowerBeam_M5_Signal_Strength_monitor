# PowerBeam_M5_Signal_Strength_monitor

This python script automates data retrieval (signal strength) from Ubiquiti PowerBeam M5 400 which uses AirMax
This Script has 3 parts

- Normal Reading
- Reading With Raspberry Pi

## Python Dependencies

```
requests
http
time
urllib3
```

### POC

![](image.png?raw=true)

#### Reading With Raspberry pi

It reading with raspberry is more difficult and require these following for the temperature , humidity and rain sensing

1. DTH11 Sensor
2. Rain Sensor
   These are used for only to increase the accuracy
