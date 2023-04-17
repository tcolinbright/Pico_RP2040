import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4
import dht
import machine

sensor = dht.DHT11(machine.Pin(4))
#pir = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
led_onboard = machine.Pin(25, machine.Pin.OUT)

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

use_imperial = True
use_PIR = False

def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    

def menu_main_temp_humidity(color_temp, color_humidity, refresh_time):
    update_numbers()
    sensor.measure()
    temp = sensor.temperature()
    temp_imperial = (int(temp) * (9/5)) + 32
    temp_imperial = round(int(temp_imperial),2)
    humidity = sensor.humidity()
    display.set_pen(color_temp)
    if use_imperial == False:
        display.text(f"{temp} °C",30,40, scale=9)
    else:
        display.text(f"{temp_imperial} °F",30,40,scale=9)
    display.set_pen(color_humidity)
    display.text(f"{humidity} %",30,130,scale=9)
    display.update()
    time.sleep(refresh_time)

def menu_main_cf(color_c, color_f, refresh_time):
    update_numbers()
    sensor.measure()
    temp = sensor.temperature()
    temp_imperial = (int(temp) * (9/5)) + 32
    temp_imperial = round(int(temp_imperial),2)
    display.set_pen(color_c)
    display.text(f"{temp} °C",30,40, scale=9)
    display.set_pen(color_f)
    display.text(f"{temp_imperial} °F",30,130,scale=9)
    display.update()
    time.sleep(refresh_time)

def menu_main_f_only(color, refresh_time):
    while True:
        if button_b.read():
            break
        else:
            update_numbers()
            sensor.measure()
            temp = sensor.temperature()
            temp_imperial = (int(temp) * (9/5)) + 32
            temp_imperial = round(int(temp_imperial),2)
            display.set_pen(color)
            display.text(f"{temp_imperial}°",45,70,scale=12)
            display.text(f"F",200,117,scale=6)
            display.update()
            time.sleep(refresh_time)
    
def menu_main_c_only(color, refresh_time):
        while True:
            if button_b.read():
                break
            else:
                update_numbers()
                sensor.measure()
                temp = sensor.temperature()
                display.set_pen(color)
                display.text(f"{temp}°",45,70,scale=12)
                display.text(f"C",200,117,scale=6)
                display.update()
                time.sleep(refresh_time)
    
def update_numbers():
    display.set_pen(BLACK)
    display.rectangle(10,10,220,220)
     

def show_large_c(color, time_on):
    clear()
    global use_imperial
    use_imperial = False
    display.set_pen(color)
    display.text(f"°C",30,50, scale=20)
    display.update()
    time.sleep(time_on)
    clear()

def show_large_f(color, time_on):
    clear()
    global use_imperial
    use_imperial = True
    display.set_pen(color)
    display.text(f"°F",30,50, scale=20)
    display.update()
    time.sleep(time_on)
    clear()

def pir_mode():
    while True:
        if button_b.read():
            break
        elif pir.value() == 1:
            menu_main_temp_humidity(WHITE, WHITE, 1)
            time.sleep(1)
        else:
            clear()


display.set_font("bitmap8")
clear()

while True:
    if button_a.read():
        if use_imperial == False:
            show_large_f(YELLOW, 3)
        else:
            show_large_c(CYAN, 3)  
    elif button_x.read():
        if use_imperial == True:
            menu_main_f_only(WHITE,1)
        else:
            menu_main_c_only(WHITE,1)

    else:
        menu_main_temp_humidity(MAGENTA, CYAN, .25)
    
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses

    


