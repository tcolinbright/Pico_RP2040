''' Reads from a 13 button IR remote.'''

import time
from machine import Pin
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

pin_ir = Pin(0, Pin.IN)
led = machine.Pin(25)


def decodeKeyValue(data):
    if data == 0x16:
        return "5"
    if data == 0x0C:
        return "7"
    if data == 0x18:
        return "2"
    if data == 0x5E:
        return "8"
    if data == 0x08:
        return "Dim -"
    if data == 0x5A:
        return "Dim +"
    if data == 0x4A:
        return "9"
    if data == 0x09:
        return "4"
    if data == 0x7:
        return "3"
    if data == 0x0D:
        return "6"
    if data == 0x44:
        return "1"
    if data == 0x43:
        return "2"
    if data == 0x45:
        led.value(1)
        return "ON"
    if data == 0x47:
        led.value(0)
        return "OFF"
    if data == 0x46:
        return "MODE"
    return "ERROR"

# User callback
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(decodeKeyValue(data))

ir = NEC_8(pin_ir, callback)  # Instantiate receiver



while True:
    
    pass

