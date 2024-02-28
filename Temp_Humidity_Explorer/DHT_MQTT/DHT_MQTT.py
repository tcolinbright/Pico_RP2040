from machine import Pin
import time
import network
import ujson
from umqtt.simple import MQTTClient
from dht import DHT22

#Define Onboard LED
led = Pin("LED", machine.Pin.OUT)

# initialize DHT22 sensor on pin 20
ths = DHT22(Pin(20))

# set update interval to 10 seconds
update_interval = 10

# connect to WiFi
ssid = "SSID"
password = "Wifi_Pass"

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

# connect to MQTT broker
mqtt_server = "server_addr"
port = 8883
client_id = 'unique_client_id'
username = 'username'
password = 'password'
topic = b"topic_name"


def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, port, user=username, password=password, keepalive=3600, ssl=True, ssl_params={'server_hostname':'api_key'})
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
 
 


# loop forever
while True:
    # read temperature and humidity data from sensor
    ths.measure()
    temperature = ths.temperature()
    humidity = ths.humidity()

    # create a dictionary with temperature and humidity data
    data = {"temperature": temperature, "humidity": humidity}

    # convert dictionary to JSON string
    json_data = ujson.dumps(data)

    # publish JSON data to MQTT topic
    
    client.publish(topic, json_data)

    # toggle light on
    led.value(0)

    # wait for update interval
    time.sleep(update_interval)
    
    # toggle led off
    led.value(1)

# disconnect from MQTT broker
client.disconnect()


