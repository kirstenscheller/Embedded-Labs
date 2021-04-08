# ECE5725 Thurs3:30 - Lab1
# ih258 and kes334

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
playing=True

while(playing):
    if not GPIO.input(27):
        print("Button 27 has been pressed")
        time.sleep(.5)
    elif not GPIO.input(22):
        print("Button 22 has been pressed")
        time.sleep(.5)
    elif not GPIO.input(23):
        print("Button 23 has been pressed")
        time.sleep(.5)
    elif not GPIO.input(17):
        print("Button 17 pressed, quitting")
        playing = False
GPIO.cleanup()

