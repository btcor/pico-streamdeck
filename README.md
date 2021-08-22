# DIY RaspberryPi Pico Stream Deck

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130341336-60d7154e-7a07-4b12-b229-f530478c4044.jpg" width="500">
</p>

This is a macro keypad built with a Raspberry Pi Pico running CircuitPython and a 3D printed enclosure and keycaps intended to act as a homemade Stream Deck, and this write up is a walkthrough of how I built it.

## Parts required

* Raspberry Pi Pico
* Cherry MX mechanical key switches
* Adafruit LED Sequins
* 3D printed enclosure

I ordered the majority of the parts, including the Pico, the LED Sequins, and the key switches, from https://www.adafruit.com.

I also 3D printed both the enclosure and the keycaps using slightly modified versions of the following designs from Thingiverse:

* https://www.thingiverse.com/thing:4186055

  I had to modify this enclosure design slightly because it was originally meant for a smaller Arduino, so it didn't fit the Raspberry Pi Pico.
  
* https://www.thingiverse.com/thing:4126150

  I slightly modified these keycaps to add a small gap at the bottom to allow the LED to shine through.
  
## Starting to put it together

The first step was to print the enclosure and insert the key switches into the faceplate.

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130339762-80292c91-238a-4796-b4bf-695441c631cc.jpg" width="500">
</p>

The next step was to add the LED Sequins to the back of the key switches. These LEDs were actually originally intended by Adafruit to be used in wearable projects, such as cosplay, and can be sewn into fabric using conductive thread. However, I discovered that these small and easy to use LEDs fit perfectly into the little gap at the bottom of the key switches. I just had to fit them into the gap at the bottom of the switch, add one drop of super glue to hold them in place, and the light would shine through the key.

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130339975-d0aeb7cd-cf6b-4402-9a73-0daecb702f3f.jpg" width="300">
</p>

I chose to give each row of buttons slightly different behavior and different colored LEDs. 

* The top row has red LEDs and they work like a toggle (pressing once turns on the LED, pressing a second time turns it off). This was meant to be assigned to mute or defean function such as muting Discord.
* The middle row has green LEDs and work like a switcher (pressing one of them turns on the LED, pressing a second button turns off the first one and turns on the new one). This was meant to work as a scene switcher.
* The bottom row has blue LEDs and only activates when pressed. This is meant to be assigned to functions such as sound alerts.

## Wiring

The Raspberry Pi Pico has 26 GPIO pins, and I used 24 of them (12 for the key switches, 12 for the LEDs). I also used the 3v3 pin (pin 36) and a ground pin (pin 38).

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130340292-61f69739-101a-4507-a44c-702a7ec8351b.png" width="700">
</p>

The first wiring I did was connect all of the top left pins of the switches. This wire will be connected to the 3v3 pin on the Pico to power the switches. The second step in the wiring was to connect the left (-) side of all of the LEDs. This wire will be connected to pin 38 on the Pico to ground the LEDs.

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130340844-a3900eae-238d-48b6-ae95-fc7cc24a57d9.jpg" width="500">
</p>

Next I soldered a wire to the right pins of each of the switches. These wires will be connected to GPIO pins on the Pico (pins 4-7, 9-12, and 14-17). Then I soldered a wire to the right (+) side of each of the LEDs. These will also be connected to GPIO pins on the Pico (pins 19-22, 24-27, 29, 31-32, and 34).

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130341207-96b11b41-25a3-4c08-99c7-718869baa5db.jpg" width="500">
</p>

## Finishing putting it together

After soldering all of the wires to the pins on the Pico, the only thing left (other that the code) was to put together the enclosure and add the keycaps to the switches. I used super glue to attach the Pico to the bottom of the enclosure making sure that it was pushed all the way to the rear so that the micro USB port was accessible through the opening in the back of the enclosure. Once the glue dries, I tucked all of the wiring into the enclosure and pushed the face plate into the front of the enclosure. 

The last step was to add the 3D printed keycaps. The keycap design that I chose is relegendable, meaning that they have a removable top that allows you to add a custom label. I printed the bottom of the keycap with grey filament and the top with transparent filament so a label would show through.

<p align="center">
  <img src="https://user-images.githubusercontent.com/8460968/130342526-bd3c893e-9cd8-4ffa-8214-34a9ac642bec.jpg" width="500">
</p>

## The code

For this project, I installed CircuitPython on the Raspberry Pi Pico. Adafruit already has a guide for installing CircuitPython at https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython. At the time of writing, the most current stable release is version 6.3.0. However, I chose to use the alpha build of 7.0.0 because this version introduced a few new features, including the ability to turn off some of the USB devices that are enabled by default. I wanted this device to be as minimally intrusive as possible, so I didn't want anything like a USB mass storage device mounted when it was plugged in. After installing CircuitPython, I had to install the Adafruit HID library to allow the Pico to interact as a keyboard. Documentation on installing libraries can be found at https://circuitpython.org/libraries. 

The code that actually makes the Stream Deck work is in the `code.py` file. In order to take advantage of the feature mentioned above allowing me to disable USB devices, I had to add the `boot.py` file, which runs immediately when the Stream Deck is plugged in. Since the code in that `boot.py` file prevents the USB mass storage device from mounting, that means that it isn't possible to access the files on the device if there is any reason to edit the code or make any changes in the future. As a safe guard for this possibility, I added the function to mount those USB devices if the bottom right button is held down when the Stream Deck is plugged in.
