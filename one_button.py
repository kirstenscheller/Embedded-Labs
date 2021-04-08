# ECE5725 Thurs3:30 - Lab1
# kes334 ih258

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while(True):
    if not GPIO.input(23):
        print("button 23 is pressed")
        time.sleep(0.2)#active low
