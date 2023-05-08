import time
from pimoroni import RGBLED


class LEDControl:
    def __init__(self, pin_r, pin_g, pin_b):
        self.led = RGBLED(pin_r, pin_g, pin_b)
        self.colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "cyan": (0, 255, 255),
            "magenta": (255, 0, 255),
            "white": (255, 255, 255),
            "purple": (128, 0, 128),
            "off": (0, 0, 0)
        }
    
    def set_color(self, color):
        rgb = self.colors.get(color.lower())
        if rgb is not None:
            self.led.set_rgb(*rgb)
    
    def flash_color(self, color, num_flashes=3, on_time=0.5, off_time=0.5):
        rgb = self.colors.get(color.lower())
        if rgb is not None:
            for i in range(num_flashes):
                self.led.set_rgb(*rgb)
                time.sleep(on_time)
                self.led.set_rgb(0, 0, 0)
                time.sleep(off_time)
    
    def error(self):
        self.flash_color("red", num_flashes=5, on_time=0.2, off_time=0.2)
    
    def connecting(self):
        self.flash_color("cyan", num_flashes=2, on_time=0.5, off_time=0.5)
    
    def connected(self):
        self.set_color("green")

