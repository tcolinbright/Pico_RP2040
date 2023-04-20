from machine import Pin
import onewire, ds18x20
import time

# Set the GPIO pins for the LEDs and temperature probe
green_led_pin = 9
red_led_pin = 22
temp_probe_pin = 2

# Set the minimum and maximum temperature values in Celsius
MIN_TEMP = 37.0
MAX_TEMP = 38.0

# Initialize the temperature probe
dat = Pin(temp_probe_pin)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds_sensor.scan()

# Initialize the GPIO pins for the LEDs
green_led = Pin(green_led_pin, Pin.OUT)
red_led = Pin(red_led_pin, Pin.OUT)

while True:
    # Take a temperature reading from the probe
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    temp_c = ds_sensor.read_temp(roms[0])
    print(temp_c)
    
    # Check if the temperature is above or below the threshold values
    if temp_c < MIN_TEMP or temp_c > MAX_TEMP:
        # Turn on the red LED and turn off the green LED
        green_led.value(0)
        red_led.value(1)
    else:
        # Turn on the green LED and turn off the red LED
        green_led.value(1)
        red_led.value(0)
    
    # Wait for 5 seconds before taking another temperature reading
    time.sleep(5)