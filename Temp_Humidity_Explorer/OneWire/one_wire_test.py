from machine import Pin
import onewire
import time
import ds18x20
from dht import DHT22

air_dht = DHT22(Pin(14))

ow = onewire.OneWire(Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

def read_dht():
    air_dht.measure()
    air_temp = air_dht.temperature()
    #print(f'DHT  {air_temp} C')
    return air_temp

def c2f(deg_c):
    temp_imperial = (int(deg_c) * (9/5)) + 32
    return temp_imperial

def probe_read():
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
       probe_temp = ds.read_temp(rom)
    
    return probe_temp

while True:
    probe_tempC = probe_read()
    probe_tempF = c2f(probe_read())
    dht_tempC = read_dht()
    dht_tempF = c2f(read_dht())
    
    print(f' Probe Temp: {probe_tempC} C  {probe_tempF} F  |  DHT: {dht_tempC} C  {dht_tempF} F')
    time.sleep(2)

