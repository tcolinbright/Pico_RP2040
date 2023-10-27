from machine import Pin
import time

class Keypad:
    def __init__(self, row_pins, col_pins):
        self.rows = [Pin(i, Pin.OUT) for i in row_pins]
        self.columns = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in col_pins]
        self.keypad_layout = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]
        self.last_key_pressed = None

    def read_keypad(self):
        for i, row in enumerate(self.rows):
            row.value(1)
            for j, column in enumerate(self.columns):
                if column.value():
                    key = self.keypad_layout[i][j]
                    if key != self.last_key_pressed:  # Prevent repetitive readings of same key
                        self.last_key_pressed = key
                        return key
            row.value(0)
        self.last_key_pressed = None
        return None

    def wait_for_keypress(self):
        '''This function will block until a key is pressed'''
        key = None
        while key is None:
            key = self.read_keypad()
            time.sleep(0.05)
        return key

# Usage:
keypad = Keypad(row_pins=[0, 1, 2, 3], col_pins=[4, 5, 6, 7])

while True:
    key = keypad.read_keypad()
    if key:
        print('Key pressed:', key)
        time.sleep(0.3)  # debounce

