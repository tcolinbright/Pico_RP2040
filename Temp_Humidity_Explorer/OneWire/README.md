# OneWire with DS18B20 and Raspberry Pi Pico
### By: Colin B.

<br><br/>

## Description
This Micropython program is designed to read the temperature values from a DS18B20 digital thermometer probe and a DHT22 air temperature and humidity sensor connected to a Raspberry Pi Pico or Pico W microcontroller board.

The program uses the machine module to control GPIO pins, the onewire module to communicate with the DS18B20 probe via 1-wire protocol, and the ds18x20 module to interface with the probe. Additionally, the program uses the dht module to read data from the DHT22 sensor.

The program contains three functions:

```read_dht()```: reads the air temperature value from the DHT22 sensor and returns it in Celsius.
```c2f()```: takes a Celsius temperature value as an input and returns the Fahrenheit equivalent.
```probe_read()```: reads the temperature value from the DS18B20 probe and returns it in Celsius.
In the main loop, the program repeatedly reads and converts temperature values in both Celsius and Fahrenheit using the functions defined earlier, and prints them to the console. The loop then waits for two seconds before repeating the process.

## Hardware Requirements
To use this program, you will need the following hardware:

-Raspberry Pi Pico or Pico W microcontroller board
-DS18B20 digital thermometer probe
-DHT22 air temperature and humidity sensor

## Usage
1. Copy and paste the code into a new file using a text editor.
1. Save the file with a .py extension.
1. Transfer the file to the Raspberry Pi Pico or Pico W board using your preferred method.
1. Connect the DS18B20 probe to GPIO pin 12 on the board.
1. Connect the DHT22 sensor to GPIO pin 14 on the board.
1. Power on the board.
1. The temperature values will be printed to the console in both Celsius and Fahrenheit units.


<br><br/>



## Walkthrough
### Importing Required Modules

The first few lines of the program import the necessary modules to work with the Raspberry Pi Pico board, the DS18B20 probe, and the DHT22 sensor. Specifically, it imports the Pin class from the machine module, the onewire and ds18x20 modules for communicating with the DS18B20 probe, and the DHT22 class from the dht module for reading data from the DHT22 sensor.

```python
from machine import Pin
import onewire
import time
import ds18x20
from dht import DHT22
```

### Initializing Sensor Objects
Next, the program initializes instances of the DHT22 and DS18X20 classes using the GPIO pins to which the sensors are connected.

```python
air_dht = DHT22(Pin(14))
ow = onewire.OneWire(Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
```

### Defining Sensor Reading Functions
The program defines three functions:

```read_dht()```: This function reads the temperature value from the DHT22 sensor by calling the measure() method, which takes a reading and stores the temperature and humidity values internally. It then retrieves the temperature value in Celsius using the temperature() method and returns it.

```c2f()```: This function takes a temperature value in Celsius as an argument and converts it to Fahrenheit using the formula (Celsius * (9/5)) + 32. It then returns the converted value.

```probe_read()```: This function reads the temperature value from the DS18B20 probe by calling the ```convert_temp()``` method to start a temperature conversion, waiting for the conversion to complete using the ```time.sleep_ms()``` method, and then calling the ```read_temp()``` method to retrieve the converted temperature value. It then returns the temperature value in Celsius.

```python
def read_dht():
    air_dht.measure()
    air_temp = air_dht.temperature()
    return air_temp

def c2f(deg_c):
    temp_imperial = (int(deg_c) * (9/5)) + 32
    return temp_imperial

def probe_read():
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
       probe_temp = ds.read_temp(rom)
    return probe_temp
```

### Main Program Loop
The main loop of the program runs continuously, reading and printing temperature values every two seconds. Within the loop, the program calls the probe_read() and read_dht() functions to obtain the temperature values in Celsius. It then calls the c2f() function to convert the temperature values to Fahrenheit. Finally, it prints the temperature values to the console in the following format:

```python
Probe Temp: {probe_tempC} C  {probe_tempF} F  |  DHT: {dht_tempC} C  {dht_tempF} F
python
Copy code
while True:
    probe_tempC = probe_read()
    probe_tempF = c2f(probe_read())
    dht_tempC = read_dht()
    dht_tempF = c2f(read_dht())
    
    print(f' Probe Temp: {probe_tempC} C  {probe_tempF} F  |  DHT: {dht_tempC} C  {dht_tempF} F')
    time.sleep(2)
```


## Conclusion

In summary, this Micropython program reads temperature data from a DHT22 sensor and a DS18B20 temperature probe connected to a Raspberry Pi Pico board. It utilizes the machine, onewire, ds18x20, and dht modules to interface with the sensors and read temperature values in Celsius. The program then converts the temperature values to Fahrenheit and prints them to the console in a human-readable format. This program can be used as a starting point for building temperature monitoring applications using these sensors with a Raspberry Pi Pico.