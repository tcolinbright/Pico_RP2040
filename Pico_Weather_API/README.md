# Weather Display using OpenWeather API and Raspberry Pi Pico W

This project uses the OpenWeather API and a Raspberry Pi Pico to display real-time weather information on a PicoGraphics display.

## Requirements

- Raspberry Pi Pico W
- Thonny IDE
- Pimoroni PicoDisplay2
- OpenWeather API key
- WiFi network with internet access

## Installation

1. Clone the repository to your local machine.
1. Open the wifi_creds.py file and enter your WiFi credentials.
1. Open the main.py file and enter your OpenWeather API key.
1. In main.py, change locations to your desired locations.
    ```python
    # Set the latitude and longitude for the location you want to get the weather for
    locations = [
        {"name": "Bellingham", "latitude": "48.75", "longitude": "-122.47"},
        {"name": "Mt. Vernon", "latitude": "48.41", "longitude": "-122.34"},
        {"name": "Anacortes", "latitude": "48.50", "longitude": "-122.62"},
        {"name": "Watsonville", "latitude": "36.91", "longitude": "-121.76"},
        {"name": "Mabton", "latitude": "46.22", "longitude": "-119.99"}
    ]
    ```
    Note: Will cycle through in order. You can add/subtract as desired.

1. Connect the PicoDisplay2 to your Raspberry Pi Pico.
1. Save main.py file to the Raspberry Pi Pico using Thonny.

## Usage

Once the program is running on the Raspberry Pi Pico, it will display weather information for several pre-defined locations on the PicoDisplay2. The RGB LED will turn green once the Pico has successfully connected to the WiFi network and retrieved the current time from the NTP server.

The program will continuously retrieve and display weather information for each location every 15 seconds.

## Functionality

The main.py file contains several functions that are used to retrieve and display weather information on the PicoGraphics display:
 - ```get_weather(latitude, longitude, api_key)```: This function makes an API call to the OpenWeather API using the provided latitude, longitude, and API key, and returns the parsed weather data as a dictionary.

- ```parse(data)```: This function extracts the relevant weather information from the parsed JSON response and returns it as a tuple.

- ```wind_direction(degrees)```: This function converts the wind direction from degrees to cardinal directions (N, NE, E, SE, etc.).

- ```time_parse(local_time)```: This function extracts the local time and date from the returned UTC time.

- ```pico_display_update()```: This function updates the PicoGraphics display with the weather information.

- ```pico_display_update2(location_name, temperature, feels_like, humidity, wind_speed, wind_card, cap_desc, lc, dd)```: This function updates the PicoGraphics display with a more detailed weather information.

- ```print_weather()```: This function prints the weather information to the console (for debugging purposes).