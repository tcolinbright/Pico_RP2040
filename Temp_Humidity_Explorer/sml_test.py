from machine import Pin, ADC
import time

sml1 = ADC(Pin(26))
sml2 = ADC(Pin(27))
sml3 = ADC(Pin(28))

while True:
    print(sml1.read_u16())
    print(sml2.read_u16())
    print(sml3.read_u16())
    print()
    time.sleep(2)