# Keypad Class for Raspberry Pi Pico

This module provides a Keypad class for interfacing with a 4x4 matrix keypad on a Raspberry Pi Pico using MicroPython.

### Dependencies:

`machine`: For handling GPIO pins.
`time`: For managing time-related functions like sleep.

### **class Keypad**:

`__init__(self, row_pins, col_pins)`:
Constructor for the Keypad class.

Parameters:

`row_pins`: List of GPIO pin numbers connected to the keypad rows.
`col_pins`: List of GPIO pin numbers connected to the keypad columns.

Attributes:

**rows**: List of Pin objects for rows initialized as outputs.

**columns**: List of Pin objects for columns initialized as inputs with pull-down resistors.

**keypad_layout**: A 2D list representing the layout of the keypad.

**last_key_pressed**: Holds the value of the last key pressed to prevent repetitive readings.

`read_keypad(self)`:
Scan the keypad for a key press.
Returns: The character of the pressed key if any key is pressed. None if no key is pressed.


`wait_for_keypress(self)`:
Waits and blocks the execution until a key is pressed.
Returns: The character of the pressed key.

### Usage:
To utilize the Keypad class, first, initialize an instance with the GPIO pin numbers connected to the keypad rows and columns.

Example:

```python
keypad = Keypad(row_pins=[0, 1, 2, 3], col_pins=[4, 5, 6, 7])
```

To continuously scan the keypad and print the detected key press:

```python
while True:
    key = keypad.read_keypad()
    if key:
        print('Key pressed:', key)
        time.sleep(0.3)  # debounce
```

Notes:
- Ensure correct wiring between the Pico and the keypad.
-Adjust the debounce time (time.sleep(0.3)) if required, depending on the specific characteristics of your keypad.
- The provided keypad layout in the class is for a standard 4x4 matrix keypad. If your keypad has a different layout, modify the keypad_layout attribute accordingly.