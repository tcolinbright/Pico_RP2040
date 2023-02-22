import machine
import time
led = machine.Pin("LED", machine.Pin.OUT)

# led.off()
# led.on()
# time.sleep(3)
# led.off()

#led.toggle()

# Define blinking function for onboard LED to indicate error codes    
def blink_onboard_led_constant(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)
 
def blink_onboard_led_rapid_pulse(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(.1)
        led.off()
        time.sleep(.1)
 
#blink_onboard_led_constant(4)
blink_onboard_led_rapid_pulse(5)