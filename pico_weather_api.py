import urequests
import ujson
import network


# Set the latitude and longitude for the location you want to get the weather for
latitude = 48.75
longitude = -122.47

#

# Set your API key
api_key = "1163e20fc8a6a2fd1acad4bf4f44d7d3"

# Connect to your local WiFi network
wifi_ssid = "Skagit Horticulture Employee"
wifi_password = "SH_14113"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)

# Wait for the connection to complete
while not wifi.isconnected():
    pass


# Make the API call and get the JSON response
url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}"
response = urequests.get(url)
data = ujson.loads(response.text)

# Check if the API call was successful
if response.status_code != 200:
    print("Error: API call failed")
    exit()

# Extract the relevant information from the JSON response
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]

# Print the weather information
print(f"Temperature: {temperature} F")
print(f"Humidity: {humidity} %")
print(f"Wind speed: {wind_speed} mph")
print(f"Description: {description}")
