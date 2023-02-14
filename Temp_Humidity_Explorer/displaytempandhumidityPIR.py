import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4
import dht
import machine

sensor = dht.DHT11(machine.Pin(4))
pir = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
led_onboard = machine.Pin(25, machine.Pin.OUT)
# We're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P4)

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)




WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
   
def flash_led():
    led_onboard.value(1)
    time.sleep(1) #this value is how long the LED is on.
    led_onboard.value(0)
    #utime.sleep(1) #this value is how long the LED is off.


def dht_sensor():
    for i in range(10):
        update_numbers()
        sensor.measure()
        temp = sensor.temperature()
        temp_imperial = (int(temp) * (9/5)) + 32
        temp_imperial = round(int(temp_imperial),2)
        humidity = sensor.humidity()
        display.set_pen(MAGENTA)
        display.text(f"Temperature:\n\n{temp} °C",30,40, scale=3)
        display.text(f"{temp_imperial} °F",120,67,scale=3)
        display.set_pen(CYAN)
        display.text(f"Humidity:\n\n{humidity} %",30,140, scale=3)
        display.update()
        time.sleep(.5)
    
    
def update_numbers():
    display.set_pen(BLACK)
    display.rectangle(30,66,180,30)
    display.rectangle(30,164,60,30)
    
# set up
clear()
display.set_font("bitmap8")
#display.set_font("sans")

led_external = machine.Pin(5, machine.Pin.OUT)

while True:
    if pir.value() == 1:
        dht_sensor()
        time.sleep(1)
    else:
        clear()
