from machine import Pin
import time

relay = Pin(18, Pin.OUT)

relay.value(1)
time.sleep(1)
relay.value(0)
print('It worked')