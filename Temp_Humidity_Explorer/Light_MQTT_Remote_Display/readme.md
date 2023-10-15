# Building a remote/wifi operated light

### Pimonorni Automation2040 as power and control board for driving lights, and a Raspberry Pi PicoW with a Pimoroni Display2 attached for a remote control with buttons and display.

#### First Steps: Light Control

Basic wiring:

Automation 2040 -
    - 12v power source + to 12v/5A PS+
    - 12v power source - to 12v/5A PS-
    - Output 1(0) to 12v PWM Light +
    - 12v PWM Light - to GND

That's it. Straight forward for a single light.

Additional USB cable to program the Pico W onboard the Automation2040.

**Note:** 
The Automation 2040 can be plugged into USB and a power source at the same time.

#### Basic Micropython Install:

Use Pimoroni's version as the libraries are already included. You can also follow their documentation how to install them through Thonny.

Setup complete! Now let's program this board. 

#### Into the code editor.

First let's make a new directory:

    mkdir /path/to/your/code/

Let's move into that directory.

    cd /path/to/your/code

Create a few utility files:

    sudo touch utilities.py ADMIN_CONFIG.py

Open `CONFIG.py`:

    nano ADMIN_CONFIG.py

Enter Wifi Creds:

    SSID = "Your SSID"
    PSK = "Password"
    COUNTRY = "US" # Change to your local two-letter ISO 3166-1 country code

Exit `ADMIN_CONFIG.py`:

    CTRL + x to  EXIT
    CTRL + Y to SAVE
    ENTER to CLOSE

### Let's build some utilities!
These functions will be needed on both ends of the hardware so might as well save code where I can. 
- Connect to WIFI
- Connect to MQTT Broker
- Subscribe to Topic(s)
- Publish to Topic(s)

Open `utilities.py`:

    nano utilities.py



### Mosquitto Install

For Ubuntu:

    sudo apt install mosquitto mosquitto-clients


To subscribe:

    mosquitto_sub {[-h host] [--unix path] [-p port] [-u username] [-P password] -t topic | -L URL [-t topic]}
    
    mosquitto_sub -h 10.0.0.184 -p 1883 -t autolight/controls


To publish:

    mosquitto_pub {[-h host] [--unix path] [-p port] [-u username] [-P password] -t topic | -L URL}
    
    mosquitto_pub -h 10.0.0.184 -p 1883 -t autolight/controls -m "ON/Test Message"