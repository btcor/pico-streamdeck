import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio


btn1_pin = board.GP2
btn2_pin = board.GP3
btn3_pin = board.GP4
btn4_pin = board.GP5
btn5_pin = board.GP6
btn6_pin = board.GP7
btn7_pin = board.GP8
btn8_pin = board.GP9
btn9_pin = board.GP10
btn10_pin = board.GP11
btn11_pin = board.GP12
btn12_pin = board.GP13

led1 = digitalio.DigitalInOut(board.GP14)
led2 = digitalio.DigitalInOut(board.GP15)
led3 = digitalio.DigitalInOut(board.GP16)
led4 = digitalio.DigitalInOut(board.GP17)
led5 = digitalio.DigitalInOut(board.GP18)
led6 = digitalio.DigitalInOut(board.GP19)
led7 = digitalio.DigitalInOut(board.GP20)
led8 = digitalio.DigitalInOut(board.GP21)
led9 = digitalio.DigitalInOut(board.GP22)
led10 = digitalio.DigitalInOut(board.GP26)
led11 = digitalio.DigitalInOut(board.GP27)
led12 = digitalio.DigitalInOut(board.GP28)

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT
led5.direction = digitalio.Direction.OUTPUT
led6.direction = digitalio.Direction.OUTPUT
led7.direction = digitalio.Direction.OUTPUT
led8.direction = digitalio.Direction.OUTPUT
led9.direction = digitalio.Direction.OUTPUT
led10.direction = digitalio.Direction.OUTPUT
led11.direction = digitalio.Direction.OUTPUT
led12.direction = digitalio.Direction.OUTPUT

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    # Top row of buttons have red LEDs and work like a toggle
    # Meant to be used for mute/deafen functions
    if btn1.value:
        keyboard.send(Keycode.SHIFT, Keycode.F13)
        print("Shift + F13 pressed")
        led1.value = not led1.value
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.SHIFT, Keycode.F14)
        print("Shift + F14 pressed")
        led2.value = not led2.value
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.SHIFT, Keycode.F15)
        print("Shift + F15 pressed")
        led3.value = not led3.value
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.SHIFT, Keycode.F16)
        print("Shift + F16 pressed")
        led4.value = not led4.value
        time.sleep(0.1)
    # Second row of buttons have green LEDS and work like a switcher
    # Meant to be used for a scene switcher
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.F13)
        print("Control + F13 pressed")
        if led5.value == True:
            led5.value = False
        else:
            led5.value = True
            led6.value = False
            led7.value = False
            led8.value = False
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.F14)
        print("Control + F14 pressed")
        if led6.value == True:
            led6.value = False
        else:
            led5.value = False
            led6.value = True
            led7.value = False
            led8.value = False
        time.sleep(0.1)
    if btn7.value:
        keyboard.send(Keycode.CONTROL, Keycode.F15)
        print("Control + F15 pressed")
        if led7.value == True:
            led7.value = False
        else:
            led5.value = False
            led6.value = False
            led7.value = True
            led8.value = False
        time.sleep(0.1)
    if btn8.value:
        keyboard.send(Keycode.CONTROL, Keycode.F16)
        print("Control + F16 pressed")
        if led8.value == True:
            led8.value = False
        else:
            led5.value = False
            led6.value = False
            led7.value = False
            led8.value = True
        time.sleep(0.1)
    # The bottom row of buttons have blue LEDS and only activate briefly when pressed
    # Meant to be used for sound alerts or other things that simply trigger when pressed
    if btn9.value:
        keyboard.send(Keycode.ALT, Keycode.F13)
        print("Alt + F13 pressed")
        led9.value = True
        time.sleep(0.25)
        led9.value = False
        time.sleep(0.1)
    if btn10.value:
        keyboard.send(Keycode.ALT, Keycode.F14)
        print("Alt + F14 pressed")
        led10.value = True
        time.sleep(0.25)
        led10.value = False
        time.sleep(0.1)
    if btn11.value:
        keyboard.send(Keycode.ALT, Keycode.F15)
        print("Alt + F15 pressed")
        led11.value = True
        time.sleep(0.25)
        led11.value = False
        time.sleep(0.1)
    if btn12.value:
        keyboard.send(Keycode.ALT, Keycode.F16)
        print("Alt + F16 pressed")
        led12.value = True
        time.sleep(0.25)
        led12.value = False
        time.sleep(0.1)
    time.sleep(0.1)
