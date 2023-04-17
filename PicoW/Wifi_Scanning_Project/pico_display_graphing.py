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
led.set_rgb(0,0,0)
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
    bssid_scanned = []
    networks = scan
    for net in networks:
        bssid = str(binascii.hexlify(net[1], ":").decode('utf-8')) #changes bytes to hex
        bssid = bssid.upper()
        dbm = net[3]
        bssid_scanned.append(bssid)
    if bssid_in in bssid_scanned:
        dbms.append(dbm)
        print(dbms)
    else:
        dbms.append(0)
        pass


scan_this_one = "DA:CB:BC:97:86:CF"

while True:
    scan = nic.scan()
    dbm_to_list(scan, scan_this_one)
    
    # fills the screen with black
    display.set_pen(BLACK)
    display.clear()


    # shifts the dbms history to the left by one sample
    if len(dbms) > WIDTH // bar_width:
        dbms.pop(0)

    i = 0

    for dbm in dbms:
        dbm_bar = (100 - abs(dbm))
       
        # chooses a pen colour
        DBM_COLOUR = GREEN
        display.set_pen(DBM_COLOUR)

        # draws the reading as a tall, thin rectangle
        display.rectangle(i, HEIGHT - (round(dbm_bar) * 4), bar_width, HEIGHT)

        # the next tall thin rectangle needs to be drawn
        # "bar_width" (default: 5) pixels to the right of the last one
        i += bar_width


    # draws a white background for the text
    display.set_pen(WHITE)
    display.rectangle(1, 1, 155, 40)

    # writes the reading as text in the white rectangle
    dbm = dbms[-1]
    display.set_pen(BLACK)
    display.text(f'dbm: {dbm}', 3, 3, scale=4)

    # time to update the display
    display.update()

    # waits for 5 seconds
    time.sleep(5)
