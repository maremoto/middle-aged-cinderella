#
# Middle-aged Cinderella software to run forever
#

import machine
import time

# Declare devices
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
pin = machine.Pin(15, machine.Pin.OUT)

# Variables
mode = 0 # 0=none, 1=mode1, 2=mode2, 3=mode3
loops_to_run = 0
current_iteration = 0
silent = 1
silent_steps = 0
vibration_steps = 0
step = 0

# Functions
def vibrate(duration=1.5):
    pin.value(1)
    time.sleep(duration)
    pin.value(0)

def doDistraction(loops=100):
    for i in range(loops):
        vibrate()
        time.sleep(.8)

def mode1_params():
    silent_steps = 20
    vibration_steps = 80
    loops_to_run = 600 # 60000

def mode2_params():
    silent_steps = 50
    vibration_steps = 50
    loops_to_run = 600 # 60000

def mode3_params():
    silent_steps = 80
    vibration_steps = 20
    loops_to_run = 600 # 60000

def switch_mode():
    current_iteration = 0
    step = 0
    silent = 1
    if mode == 0:
        mode = 1
        mode1_params()
    elif mode == 1:
        mode = 2
        mode2_params()
    elif mode == 2:
        mode = 3
        mode3_params()
    else:
        mode = 0

# Main loop, button surveillance
while True:
    first = button.value()
    time.sleep(0.01)
    step += 1
    second = button.value()
    #if first and not second:
    #    print('Button pressed!')
    #else
    if not first and second:
        #print('Button released!')
        switch_mode()

    # Silence
    if mode == 0:
        pin.value(0)
        continue

    # Vibration mode 1,2,3
    if silent:
        if step > silent_steps:
            silent = 0
            step = 0
            pin.value(1)
    else:
        if step > vibration_steps:
            silent = 1
            step = 0
            pin.value(0)

