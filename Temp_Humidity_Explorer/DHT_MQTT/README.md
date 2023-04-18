# DHT_MQTT Documentation
## Overview

This program is written in MicroPython and designed to run on a Raspberry Pi Pico W board with a DHT22 temperature and humidity sensor. The program connects to a Wi-Fi network and an MQTT broker to publish temperature and humidity data to a specified MQTT topic.

The program periodically reads temperature and humidity data from the DHT22 sensor, converts the data to a JSON string, and publishes it to the specified MQTT topic. The LED on the board is also toggled on and off to indicate when data is being published.
Requirements

- Raspberry Pi Pico W board
- DHT22 temperature and humidity sensor
- Wi-Fi network credentials (SSID and password)
- MQTT broker credentials (server address, port number, client ID, username, password, and topic name)

<br><br/>

## Installation

To run this program, follow these steps:

1. Connect the DHT22 sensor to the Raspberry Pi Pico W board, ensuring that the correct pin is specified in the code.

1. Connect the Raspberry Pi Pico W board to a computer with MicroPython installed.

1. In Thonny Navigate to Tools > Manage Packages
    - Search for and install the  "micropython-mqtt.simple" package.
    - Verify by trying to import the mqtt.simple library in the REPL.
    ```python
    from mqtt.simple import MQTTClient
    ```

1. If no errors, copy and paste the code into a new file using your preferred code editor, and save the file with a .py extension.

1. Update the program variables to match your Wi-Fi and MQTT broker credentials.

1. Save the changes to the file.

1. Copy the file onto the Raspberry Pi Pico W board using Thonny.

1. Reset the Raspberry Pi Pico W board to run the program.

## Usage

When the program is running, it will connect to the specified Wi-Fi network and MQTT broker. It will then read temperature and humidity data from the DHT22 sensor, convert the data to a JSON string, and publish it to the specified MQTT topic. The LED on the board will be toggled on and off to indicate when data is being published.

The program will run indefinitely until it is manually stopped or the board loses power.
Troubleshooting

If the program fails to connect to the Wi-Fi network or MQTT broker, it will print an error message and attempt to reconnect after a 5 second delay. If reconnection is successful, the program will resume normal operation. If reconnection fails multiple times, the board will reset.

If the DHT22 sensor is not connected or is malfunctioning, the program will not be able to read temperature and humidity data, and no data will be published to the MQTT topic.





<br><br/>

## Code Walk Through

Import necessary modules and libraries.

```python
from machine import Pin
import time
import network
import ujson
from umqtt.simple import MQTTClient
from dht import DHT22
```

Define the onboard LED and the DHT22 sensor on pin 20.


```python
led = Pin("LED", machine.Pin.OUT)
ths = DHT22(Pin(20))
```

Set the update interval to 10 seconds.

```python
update_interval = 10
```


Connect to the Wi-Fi network using the specified SSID and password.


```python
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
```

Connect to the specified MQTT broker using the specified credentials.


```python
mqtt_server = "server_addr"
port = 8883
client_id = 'unique_client_id'
username = 'username'
password = 'password'
topic = b"topic_name"
```


Define functions for connecting to and reconnecting to the MQTT broker. 
Note: In the paramaters of MQTTClient(ssl_params=) in this case is the same as the server_addr.

```python
def mqtt_connect():
    client = MQTTClient(client_id,
                         mqtt_server, 
                         port, 
                         user=username, 
                         password=password, 
                         keepalive=3600, 
                         ssl=True, 
                         ssl_params={'server_hostname':'server_addr'}
                         )
    
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()
```

Attempt to connect to the MQTT broker, and if unsuccessful, attempt to reconnect.

```python
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
```

Loop forever, reading temperature and humidity data from the DHT22 sensor, converting it to a JSON string, and publishing it to the specified MQTT topic.


```python
while True:
    ths.measure()
    temperature = ths.temperature()
    humidity = ths.humidity()

    data = {"temperature": temperature, "humidity": humidity}
    json_data = ujson.dumps(data)
    client.publish(topic, json_data)

    led.value(0)
    time.sleep(update_interval)
    led.value(1)
```

Disconnect from the MQTT broker if connection breaks.


```python
client.disconnect()
```

<br><br/>

## **Full Code:**

```python
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
    client = MQTTClient(client_id, mqtt_server, port, user=username, password=password, keepalive=3600, ssl=True, ssl_params={'server_hostname':'server_addr'})
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



```



<br><br/>

