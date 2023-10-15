from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2
from pimoroni import Button
from ADMIN_CONFIG import *
from utilities import *

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2)

display.set_backlight(0.5)
display.set_font("bitmap8")

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


# Connect to WiFi
connect_to_network(SSID, PSK)

# Connect to MQTT Broker
client = mqtt_connect(client_id, mqtt_server, port)


while True:
    topic = "autolight/controls"
    if button_a.read():
        msg_a = "ON"
        client.publish(topic, msg_a)
    elif button_b.read():
        msg_b = "OFF"
        client.publish(topic, msg_b)