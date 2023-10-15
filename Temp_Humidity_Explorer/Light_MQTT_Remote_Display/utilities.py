import time
import network
import ujson
from umqtt.simple import MQTTClient
from ADMIN_CONFIG import *




# Connect to WiFi Network
def connect_to_network(ssid, password):

    station = network.WLAN(network.STA_IF)
    print(f'Attempting to Connect to:  {ssid}')
    station.active(True)

    try:
        station.connect(ssid, password)
    except OSError as e:
        print(e)
    while not station.isconnected():
        time.sleep(1)

    print("Connected to WiFi")
    print(station.ifconfig())

# EX: connect_to_network(SSID, PSK)




# Connect to MQTT Broker

def mqtt_connect(client_id, mqtt_server, port):
    '''Connect to broker'''
    try:
        client = MQTTClient(client_id, mqtt_server, port, keepalive=3600)
        client.connect()
        print('Connected to %s MQTT Broker'%(mqtt_server))
    except OSError as e:
        reconnect()
    
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(2)
   
# EX: mqtt_connect(client_id, mqtt_server, port)
 
