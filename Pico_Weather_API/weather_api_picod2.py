import urequests
import time
import ntptime
import ujson
import network
from wifi_creds import *
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
RED = dp.create_pen(255, 0, 0)


# Set the latitude and longitude for the location you want to get the weather for
locations = [
    {"name": "Bellingham", "latitude": "48.75", "longitude": "-122.47"},
    {"name": "Mt. Vernon", "latitude": "48.41", "longitude": "-122.34"},
    {"name": "Anacortes", "latitude": "48.50", "longitude": "-122.62"},
    {"name": "Watsonville", "latitude": "36.91", "longitude": "-121.76"},
    {"name": "Mabton", "latitude": "46.22", "longitude": "-119.99"}
]


# Connect to your local WiFi network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)
led.set_rgb(0,255,0)

# Wait for the connection to complete
while not wifi.isconnected():
    pass

# Connect to NTP server to get current time
ntptime.settime()


def get_weather(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}"
    response = urequests.get(url)
    data = ujson.loads(response.text)

    if response.status_code == 200:
        #print(data) # Check API Response in terminal
        return data
    else:
        raise Exception("Error: API call failed")



# Extract the relevant information from the JSON response
def parse(data):
    location = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_dir = data["wind"]["deg"]
    description = data["weather"][0]["description"]
    return temperature, feels_like, humidity, wind_speed, wind_dir, description


# Convert Wind Direction Degrees to Cardinal Directions
def wind_direction(degrees):
    cardinal_directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    idx = int(round((degrees % 360) / (360. / len(cardinal_directions))))
    return cardinal_directions[idx % len(cardinal_directions)]


# Get Date and Time
def time_parse(local_time):
    year = local_time[0]
    month = local_time[1]
    mday = local_time[2]
    hour = local_time[3]
    minute = local_time[4]
    second = local_time[5]
    weekday = local_time[6]
    yearday = local_time[7]
    
    local_clock = f"{hour:02}:{minute:02}"
    display_date = f"{month:02}-{mday:02}-{year}"
    
    return local_clock, display_date


# To clear the display
def clear():
    dp.set_pen(BLACK)
    dp.clear()
    dp.update()


# Print the weather information
def print_weather(location_name, temperature, feels_like, humidity, wind_speed, wind_card, cap_desc):
    print(f"{location_name}")
    print(f"Temperature: {temperature} F")
    print(f"Feels Like: {feels_like} F")
    print(f"Humidity: {humidity} %")
    print(f"Description: {cap_desc}")
    print(f"Wind Dir: {wind_dir} Deg")
    print(f"Wind Card: {wind_card}")
    print(f"Wind speed: {wind_speed} mph")
    print()
   
    
#Display to screen:
def pico_display_update2(location_name, temperature, feels_like, humidity, wind_speed, wind_card, cap_desc, lc, dd):
    clear()
    led.set_rgb(0,0,0)
    
    # Location
    dp.set_pen(GREEN)
    dp.text(f"{location_name}", 25, 10, scale=3)
    
    # Date and Time
    dp.set_pen(MAGENTA)
    dp.text(f"{dd}", 195, 5, scale=2)
    dp.set_pen(WHITE)
    dp.text(f"{lc}", 210, 30, scale=3)
    
    # Temperature
    dp.set_pen(RED)
    #dp.text(f"{temperature} F", 225, 20, scale=3)
    dp.text("Feels Like:", 25, 65, scale=2)
    dp.text(f"{feels_like} F", 25, 95, scale=3)
    
    # Humidity
    dp.set_pen(CYAN)
    dp.text("Humidity:", 190, 65, scale=2)
    dp.text(f"{humidity} %", 200, 95, scale=3)
    
    # Wind Speed and Direction
    dp.set_pen(YELLOW)
    dp.text("Wind Dir:", 25, 135, scale=2)
    dp.text(f"{wind_card}", 30, 160, scale=3)
    dp.text("Wind Speed:", 190, 135, scale=2)
    dp.text(f"{wind_speed} mph", 190, 160, scale=3)
    
    # Sky Description
    dp.set_pen(WHITE)
    dp.text(f"{cap_desc}.", 80, 200, scale=2)
    dp.update() 


# Loop through each location in locations list.
while True:
    for location in locations:
        # Make the API call and parse the response
        weather_data = parse(get_weather(location["latitude"], location["longitude"], api_key))

        # Extract the relevant information from the returned tuple
        location_name = location["name"]
        temperature, feels_like, humidity, wind_speed, wind_dir, description = weather_data

        # Convert wind_dir into cardinal direction
        wind_card = wind_direction(wind_dir)
        cap_desc = description.upper()
        
        # Get the date and time
        UTC_OFFSET = -7 * 60 * 60  # Adjust time zone
        current_local = time.localtime(time.time() + UTC_OFFSET)
        lc, dd = time_parse(current_local)

        # Display on pico
        pico_display_update2(location_name, temperature, feels_like, humidity, wind_speed, wind_card, cap_desc, lc, dd)
        #print_weather(location_name, temperature, feels_like, humidity, wind_speed, wind_card, cap_desc)

        # Wait
        time.sleep(15)



