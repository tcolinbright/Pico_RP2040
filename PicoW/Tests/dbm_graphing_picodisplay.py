'''Change to log dbm strengths from pico w'''
import machine
import time
from pimoroni import RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY

# set up the hardware
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)

led = RGBLED(6, 7, 8)

# set the display backlight to 50%
display.set_backlight(0.5)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)


dbm_min = 10
dbm_max = 30
bar_width = 5

dbms = []

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


while True:
    # fills the screen with black
    display.set_pen(BLACK)
    display.clear()

    dbm = #Function here from pico W wifi scanner
    #Will append dbm reading to dbms list
   
    # shifts the dbm history to the left by one sample
    if len(dbms) > WIDTH // bar_width:
        dbms.pop(0)

    i = 0

    for t in dbms:
        # chooses a pen colour based on the dbm
        DBM_COLOUR = display.create_pen(*dbm_to_color(t))
        display.set_pen(DBM_COLOUR)

        # draws the reading as a tall, thin rectangle
        display.rectangle(i, HEIGHT - (round(t) * 4), bar_width, HEIGHT)

        # the next tall thin rectangle needs to be drawn
        # "bar_width" (default: 5) pixels to the right of the last one
        i += bar_width


    # draws a white background for the text
    display.set_pen(WHITE)
    display.rectangle(1, 1, 100, 25)

    # writes the reading as text in the white rectangle
    display.set_pen(BLACK)
    display.text("{:.2f}".format(dbm) + "dbm", 3, 3, 0, 3)

    # time to update the display
    display.update()

    # waits for 5 seconds
    time.sleep(5)