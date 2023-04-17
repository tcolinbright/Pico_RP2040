from machine import Pin
from dht import DHT11

wx = DHT11(Pin(4))

wx.measure()
temp = wx.temperature()
tempF = (int(temp) * (9/5)) + 32
tempF = round(int(tempF),2)
rh = int(wx.humidity())


dew_pt = (temp - ((100 - rh)/5))


print(f'{temp} C / {tempF} F')
print(f'{rh} % RH  /  {dew_pt} C Dew Point')