# middle-aged-cinderella
Software for Hackster.io project Middle-aged Cinderella

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/maremoto/middle-aged-cinderella/blob/master/LICENSE)

This MicroPython code performs the functionality of the device.

## Features
When the button is pressed, the device initiates a sequence of vibrations in mode1, if it is pressed again without ending it goes to mode2, also for mode3, a new press stops the sequence.
Each mode has a different pattern of vibrations and a different duration.

## Full Installation
### Prerequisites: MicroPython
The first step is loading the MicroPython onto the Adafruit Feather HUZZAH ESP8266, you can follow the instructions [here](https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266?embeds=allow).

### Prerequisites: Ampy
You must install Ampy in your computer to deploy the software onto the Feather board.
```bash
pip install adafruit-ampy
```
### Installation to Feather board
Installation is very simple, the software is downloaded from this repository and transferred to the device.
```bash
git clone https://github.com/maremoto/middle-aged-cinderella.git
cd middle-aged-cinderella
ampy -p /dev/tty.SLAB_USBtoUART -b 115200 put main.py
ampy -p /dev/tty.SLAB_USBtoUART -b 115200 reset
```
You must replace ```/dev/tty.SLAB_USBtoUART``` with your path or name of the serial port connected to the MicroPython board.
The ```main.py``` if exists it's automatically run after ```boot.py``` and starts the functionality loop.
