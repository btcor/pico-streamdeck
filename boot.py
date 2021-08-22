import storage, usb_cdc
import board, digitalio

# Declare the variables for the 12th button
btn12_pin = board.GP13
btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.pull = digitalio.Pull.DOWN

# Hold down the bottom right button when you plug in the Stream Deck 
# to enable the USB mass storage device in order to edit files
if not btn12.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
