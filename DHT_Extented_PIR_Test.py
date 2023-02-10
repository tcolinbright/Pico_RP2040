'''This displays temperature and humidty data from the DHT11 and displays it to the 240x240 LCD on the Pico_Explorer
General functionality of buttons
a = change c/f (from main menu)
b = back (from main menu it will display C and F)
x = display F or C only
y = pir mode for given menu'''



import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4
import dht
import machine

sensor = dht.DHT11(machine.Pin(4)) #Assign pn for DHT11
pir = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP) #Assign pin for PIR sensor
led_onboard = machine.Pin(25, machine.Pin.OUT) #Assign pin for onboard LED
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P4) #define the display

#Assign Buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

#Create colors
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)
BLUE = display.create_pen(0, 0, 255)

#Global Variables
pir_color = WHITE
use_imperial = True


def clear(): #shortcut to wipe the screen (flashes)
    display.set_pen(BLACK)
    display.clear()
    display.update()
    

def menu_main_temp_humidity(color_temp, color_humidity, refresh_time): #Main menu to display
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

def menu_main_cf(color_c, color_f, refresh_time): #Displays both C and F
    while True:
        if button_b.read():
            break
        elif button_y.read():
            pir_mode(menu_main_cf(pir_color, pir_color, 1))
        else:
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

def menu_main_f_only(color, refresh_time): #Shows on F
    while True:
        if button_b.read():
            break
        elif button_y.read():
            pir_mode(menu_main_f_only(pir_color, 1))
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
    
def menu_main_c_only(color, refresh_time): #Shows only C
        while True:
            if button_b.read():
                break
            elif button_y.read():
                pir_mode(menu_main_c_only(pir_color, 1))
            else:
                update_numbers()
                sensor.measure()
                temp = sensor.temperature()
                display.set_pen(color)
                display.text(f"{temp}°",45,70,scale=12)
                display.text(f"C",200,117,scale=6)
                display.update()
                time.sleep(refresh_time)
    
def update_numbers(): #colors screen black, doesn't flash the screen.
    display.set_pen(BLACK)
    display.rectangle(10,10,220,220)
    
    
#def cycle_colors():
  #move colors to a list to cycle through with a for loop
    #change local variable by 1.

def show_large_c(color, time_on): #Graphic to display when selecting C as temp
    clear()
    display.set_pen(color)
    display.text(f"°C",30,50, scale=20)
    display.update()
    time.sleep(time_on)
    clear()

def show_large_f(color, time_on): #Graphic to display when selecting F as temp
    clear()
    display.set_pen(color)
    display.text(f"°F",30,50, scale=20)
    display.update()
    time.sleep(time_on)
    clear()

def pir_mode(func): #runs the menu but with pir color, only displays when motion detected
    while True:
        if button_b.read():
            break
        elif pir.value() == 1:
            func()
            time.sleep(1)
        else:
            clear()


def change_cf_mode(): #Changes global variable to change if C or F is displayed.
    if use_imperial == False:
        global use_imperial
        use_imperial = True
        show_large_f(YELLOW, 3)

    else:
        global use_imperial
        use_imperial = False 
        show_large_c(CYAN, 3) 


def menu_switch_cf(): #Shortcut to choose which menu to display based on global variable use_imperial
    if use_imperial == True:
        menu_main_f_only(WHITE,1)
    else:
        menu_main_c_only(WHITE,1)

##  Start ##



#Setup display and pick font
display.set_font("bitmap8")
clear()

while True: #Cycles through code waiting for button to be pressed.
    if button_a.read():
        change_cf_mode()

    elif button_x.read():
        menu_switch_cf()

    elif button_y.read():
        pir_mode(menu_main_temp_humidity(pir_color, pir_color, 1))

    elif button_b.read():
        menu_main_cf(RED, BLUE, 1)
        
    else:
        menu_main_temp_humidity(MAGENTA, CYAN, .25)
    
    time.sleep(0.1)  
