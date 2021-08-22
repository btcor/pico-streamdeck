import storage, usb_cdc
import board, digitalio

btn12_pin = board.GP13
btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.pull = digitalio.Pull.DOWN

if not btn12.value:
    storage.disable_usb_drive()
    usb_cdc.disable()