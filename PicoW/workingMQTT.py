import network
import time
from machine  import Pin
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...\n')
    wlan.connect("SSID", "Password")
    while not wlan.isconnected():
         pass

print(wlan.isconnected())


mqtt_server = "mqtt_server"
port = 8883
client_id = 'picofromshowerdht22'
username = 'mqtt_username'
password = 'mqtt_password'
topic_pub = 'test'
topic_msg = 'Testmessage'

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, port, user=username, password=password, keepalive=3600, ssl=True, ssl_params={'server_hostname':'servername'})
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
