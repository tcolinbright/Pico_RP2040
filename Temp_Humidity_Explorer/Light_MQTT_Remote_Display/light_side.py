from ADMIN_CONFIG import *
from utilities import *
from automation import Automation2040W
import time


# STATES
O1_STATE = False # Status of Ouput 1

# Initialize Board
board = Automation2040W()

# Connect to WiFi
connect_to_network(SSID, PSK)


def control_cb(topic, msg):
    msg = msg.decode('ascii')
    if msg == "ON":
        board.output(0,100)
        O1_STATE = True
        print("ON")
    elif msg == "OFF":
        board.output(0,0)
        O1_STATE = False
        print("OFF")
    else:
        print(msg)
      
   


# Connect to MQTT Broker
client = mqtt_connect(client_id, mqtt_server, port)
client.set_callback(control_cb)
client.subscribe("autolight/controls")

while True:
   msg = client.check_msg()
   print(msg)
   time.sleep(.5)
