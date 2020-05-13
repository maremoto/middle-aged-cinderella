#
# Middle-aged Cinderella software to run forever
#

import machine
import time

TEST_MODE = False

# Declare devices
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
pin = machine.Pin(15, machine.Pin.OUT)

# Variables
global mode, loops_to_run, silent_steps, vibration_steps, step, silent, current_iteration
mode = 0 # 0=none, 1=mode1, 2=mode2, 3=mode3
loops_to_run = 0
current_iteration = 0
silent = 1
silent_steps = 0
vibration_steps = 0
step = 0

# Mode config
def mode1_params():
    global silent_steps, vibration_steps, loops_to_run
    silent_steps = 80
    vibration_steps = 20
    if TEST_MODE:
        loops_to_run = 600
    else:
        loops_to_run = 60000

def mode2_params():
    global silent_steps, vibration_steps, loops_to_run
    silent_steps = 100
    vibration_steps = 50
    if TEST_MODE:
        loops_to_run = 600
    else:
        loops_to_run = 60000

def mode3_params():
    global silent_steps, vibration_steps, loops_to_run
    silent_steps = 200
    vibration_steps = 80
    if TEST_MODE:
        loops_to_run = 600
    else:
        loops_to_run = 60000

# Helpers
def switch_mode():
    global mode, current_iteration, step, silent
    current_iteration = 0
    step = 0
    silent = 0
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
        silent = 1

# Main loop, button surveillance
while True:
    first = button.value()
    time.sleep(0.01)
    current_iteration += 1
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

    if current_iteration > loops_to_run:
        mode = 0
