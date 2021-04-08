#ECE5725 Th330 Lab
#more_video_control.py
# kes334 ih258

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
playing = True

while (playing):
    time.sleep(0.2)
    if not GPIO.input(27):
        print ("paus has been npressed")
        os.system('echo "pause" > /home/pi/test_fifo')
        
    elif not GPIO.input(23):
        print("right has een prssed")
        os.system('echo "seek 10" > /home/pi/test_fifo')
        
    elif not GPIO.input(22):
        os.system('echo "seek -10" > /home/pi/test_fifo')

    elif not GPIO.input(26):
        os.system('echo "seek 30" > /home/pi/test_fifo')

    elif not GPIO.input(19):
        os.system('echo "seek -30" > /home/pi/test_fifo')
        
    elif not GPIO.input(17):
        os.system('echo "q" > /home/pi/test_fifo')
        playing = False
        
GPIO.cleanup()
