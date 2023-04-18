# **Micropython Temperature Monitoring Program**

This Micropython program uses a DS18B20 temperature probe and controls a green LED and a red LED based on the temperature readings. The program takes a temperature reading from the probe every 5 seconds and turns on the green LED if the temperature is within a certain range, and turns on the red LED if the temperature is outside that range. 

## **Hardware Requirements**

This program requires the following components:
- DS18B20 temperature probe
- Green LED
- Red LED
- Resistors (if necessary)
- Wires
- Microcontroller board (e.g., ESP8266, ESP32, or similar)

## **Software Requirements**

This program requires the following software:
- Micropython firmware installed on the microcontroller board
- A text editor to write and edit the program

## **Setting up the Circuit**

Connect the DS18B20 temperature probe to the microcontroller board using the OneWire protocol. Connect the green LED to a GPIO pin on the board and connect the red LED to another GPIO pin on the board. If necessary, use resistors to limit the current flow to the LEDs.

## **Program Walkthrough**

The program consists of the following steps:

### **Step 1: Importing necessary modules and setting up GPIO pins**

```python
import machine import Pin
import onewire, ds18x20
import time

# Set the GPIO pins for the LEDs and temperature probe
green_led_pin = 4
red_led_pin = 5
temp_probe_pin = 2

# Set the minimum and maximum temperature values in Celsius
MIN_TEMP = 20
MAX_TEMP = 30

# Initialize the temperature probe
dat = Pin(temp_probe_pin)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds_sensor.scan()

# Initialize the GPIO pins for the LEDs
green_led = Pin(green_led_pin, Pin.OUT)
red_led = Pin(red_led_pin, Pin.OUT)
```

The first step of the program is to import the necessary modules and set up the GPIO pins for the LEDs and the temperature probe. The program sets the minimum and maximum temperature values that we want to use as thresholds for turning on the LEDs.

The program then initializes the temperature probe and the GPIO pins for the LEDs using the machine.Pin function. The temperature probe is set up using the OneWire protocol and the ds18x20.DS18X20 function.

### **Step 2: Reading the temperature from the probe**
```python
while True:
    # Take a temperature reading from the probe
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    temp_c = ds_sensor.read_temp(roms[0])
```

The program uses a while loop to continuously take temperature readings from the probe. The program uses the ds_sensor.convert_temp() function to start a temperature conversion and the time.sleep_ms(750) function to wait for the conversion to complete. The program then reads the temperature value from the probe using the ds_sensor.read_temp(roms[0]) function.

### **Step 3: Controlling the LEDs based on the temperature reading**


```python
    # Check if the temperature is above or below the threshold values
    if temp_c < MIN_TEMP or temp_c > MAX_TEMP:
        # Turn on the red LED and turn off the green LED
        green_led.value(0)
        red_led.value(1)
    else:
        # Turn on the green LED and turn off the red LED
        green_led.value(1)
        red_led.value(0)
 ```


The program checks if the temperature reading is above or below the threshold values. If the temperature is above or below MAX/MIN TEMP the Red LED is illuminated. If between the values, the Green LED is illuminated.

Finally, the program pauses to not over tax the temperature probe.

```python
      # Wait for 5 seconds before taking another temperature reading
    time.sleep(5)
```