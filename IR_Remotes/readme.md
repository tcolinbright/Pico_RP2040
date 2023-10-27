# IR Remote Decoder for a 13-Button Remote

Requires the IR library found here:

https://github.com/peterhinch/micropython_ir/tree/master



This program decodes the signals from a 13-button IR remote using the NEC protocol. The decoded button presses are then printed to the console.

### Dependencies:
`ir_rx.print_error`: A module providing error printing functionality.
`ir_rx.nec`: A module for handling the NEC infrared communication protocol.

### Hardware Setup:
An IR receiver is connected to the GPIO pin 0 of the board.
Onboard LED is connected to GPIO pin 25, which can be toggled ON and OFF using the remote.

### Functions:
`decodeKeyValue(data: int)` -> str

Decodes the given data value received from the IR remote into a corresponding button label.

Parameters:

data (int): The value to be decoded.
Returns:

A string representing the button label. Returns "ERROR" if the data doesn't correspond to any known button.
callback(data: int, addr: int, ctrl: int)

The callback function to handle the decoded IR signals.

Parameters:

data (int): The data value received from the IR remote.
addr (int): The address from which the data is received. (Not used in this implementation.)
ctrl (int): Control data received. (Not used in this implementation.)

### Functionality:

If a valid button press is detected (i.e., not a repeat code), this function will decode the button using decodeKeyValue and print the result.
If the "ON" button is pressed, the LED is turned ON.
If the "OFF" button is pressed, the LED is turned OFF.

### Execution:
Upon running the program, it waits for an IR signal. When a button on the remote is pressed, the decoded value is printed to the console. If the button corresponds to "ON" or "OFF", the LED's state will be changed accordingly.

**Note**:
The program uses a continuous loop (while True: pass) to keep running and listening for IR signals indefinitely.