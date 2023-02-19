'''Change to log dbm strengths from pico w'''
import machine
import network
import binascii
import time
from pimoroni import RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY

# set up the hardware
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)
nic = network.WLAN(network.STA_IF)
nic.active(True)

led = RGBLED(6, 7, 8)

# set the display backlight to 50%
display.set_backlight(0.5)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)


dbm_min = -90
dbm_max = -10
bar_width = 5

dbms = [] # Empty list of -dbm readings

colors = [(0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]


def dbm_to_color(dbm):
    dbm = min(dbm, dbm_max)
    dbm = max(dbm, dbm_min)

    f_index = float(dbm - dbm_min) / float(dbm_max - dbm_min)
    f_index *= len(colors) - 1
    index = int(f_index)

    if index == len(colors) - 1:
        return colors[index]

    blend_b = f_index - index
    blend_a = 1.0 - blend_b

    a = colors[index]
    b = colors[index + 1]

    return [int((a[i] * blend_a) + (b[i] * blend_b)) for i in range(3)]


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


    if len(dbms) > WIDTH // bar_width:
        dbms.pop(0)

    i = 0

    for dbm in dbms:
        # chooses a pen colour based on the dbm
        DBM_COLOUR = display.create_pen(*dbm_to_color(dbm))
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
    #display.set_pen(BLACK)
    #display.text("{:.2f}".format(dbm) + "dbm", 3, 3, 0, 3)

    # time to update the display
    display.update()

    # waits for 5 seconds
    time.sleep(5)