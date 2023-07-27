import time
import badger2040
import badger_os

display = badger2040.Badger2040()
display.led(128)
display.update_speed(badger2040.UPDATE_NORMAL)

# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT
print(f"Badger Pico Display size:\n{WIDTH}px x {HEIGHT} px")


def wipe_screen(): # shakes the etch-a-sketch
    display.pen(15)
    display.clear()
    #display.update()
    
    
def test_text(font ,text, x, y, scale_in):
    '''Displays sample text.'''
    display.pen(0)
    display.font("bitmap8")
    display.text("WHOLE",81, 63, scale=2)
    display.font(font)
    display.text(text, x, y, scale=scale_in)
    #display.update()
    
    
def small_test_text(font ,text, x, y, scale_in):
    '''Displays sample text.'''
    display.pen(0)
    display.font("bitmap8")
    display.font(font)
    display.text(text, x, y, scale=scale_in)
    
def out_final_out():
    '''Clears the screen. Adds buffered text to screen. Updates screen.'''
    wipe_screen()
    small_test_text("bitmap8", "WHOLE", 81, 63, 2)
    test_text("bitmap14_outline", "Brenda's\nWorld", 40, 7, 4)    
    display.update()

out_final_out()
