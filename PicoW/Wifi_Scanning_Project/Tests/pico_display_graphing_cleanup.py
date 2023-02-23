# This example takes the temperature from the Pico's onboard temperature sensor, and displays it on Pico Display Pack, along with a little pixelly graph.
# It's based on the thermometer example in the "Getting Started with MicroPython on the Raspberry Pi Pico" book, which is a great read if you're a beginner!

import network
import binascii
import time
from pimoroni import RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2

# set up the hardware
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, rotate=0)
led = RGBLED(6, 7, 8) # Pins 6, 7, 8 control R, G, B
nic = network.WLAN(network.STA_IF)
nic.active(True)
# set the display backlight to 50%
display.set_backlight(0.5)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
GREEN = display.create_pen(0, 255, 0)


bar_width = 5

dbms = []


def dbm_to_list(scan, bssid_in):
    '''Filter scan for BSSID and log dbm to list'''
    networks = scan
    for net in networks:
        bssid = str(binascii.hexlify(net[1], ":")) #changes bytes to hex
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")
        dbm = str(net[3])
        if bssid == bssid_in:
            dbms.append(dbm)
        else:
            print(f'{bssid_in} not located...')

scan_this_one = ""

while True:
    scan = nic.scan()
    dbm_to_list(scan, scan_this_one)
    
    # fills the screen with black
    display.set_pen(BLACK)
    display.clear()

    # the following two lines do some maths to convert the number from the temp sensor into celsius
    #Append to list of dbms here

    #temperatures.append(temperature)

    # shifts the temperatures history to the left by one sample
    if len(dbms) > WIDTH // bar_width:
        dbms.pop(0)

    i = 0

    for dbm in dbms:
        # chooses a pen colour based on the temperature
        DBM_COLOUR = BLACK
        display.set_pen(DBM_COLOUR)

        # draws the reading as a tall, thin rectangle
        display.rectangle(i, HEIGHT - (round(dbm) * 4), bar_width, HEIGHT)

        # the next tall thin rectangle needs to be drawn
        # "bar_width" (default: 5) pixels to the right of the last one
        i += bar_width


    # draws a white background for the text
    display.set_pen(WHITE)
    display.rectangle(1, 1, 100, 25)

    # writes the reading as text in the white rectangle
    display.set_pen(BLACK)
    #display.text("{:.2f}".format(dbm) + "c", 3, 3, 0, 3)

    # time to update the display
    display.update()

    # waits for 5 seconds
    time.sleep(5)