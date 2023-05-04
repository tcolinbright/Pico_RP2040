import urequests
import ujson
import network
from pimoroni import RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2


# Setup Display
dp = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2)
dp.set_font("bitmap8")
dp.set_backlight(0.7)
led = RGBLED(6, 7, 8)
led.set_rgb(255,0,255)

# Define some colors to use
WHITE = dp.create_pen(255, 255, 255)
BLACK = dp.create_pen(0, 0, 0)
CYAN = dp.create_pen(0, 255, 255)
MAGENTA = dp.create_pen(255, 0, 255)
YELLOW = dp.create_pen(255, 255, 0)
GREEN = dp.create_pen(0, 255, 0)


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


def get_weather(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}"
    response = urequests.get(url)
    data = ujson.loads(response.text)
    return data

    # Check if the API call was successful
    if response.status_code != 200:
        print("Error: API call failed")
        exit()


# Extract the relevant information from the JSON response
def parse(data):
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    return temperature, humidity, wind_speed, description

# To clear the display
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

# Make the API call and parse the response
weather_data = parse(get_weather(latitude, longitude, api_key))

# Extract the relevant information from the returned tuple
temperature, humidity, wind_speed, description = weather_data

# Print the weather information
print(f"Temperature: {temperature} F")
print(f"Humidity: {humidity} %")
print(f"Wind speed: {wind_speed} mph")
print(f"Description: {description}")

#Display to screen:
dp.clear()
dp.set_pen(WHITE)
dp.text(f"{temperature} F", 25, 25, scale=3)
dp.text(f"{humidity} %", 200, 25, scale=3)
dp.text(f"Wind speed: {wind_speed} mph", 25, 125, scale=3)
dp.text(f"{description}.", 25, 175, scale=3)
dp.update()