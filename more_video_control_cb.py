#ECE 5725 Thursday Lab
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

def callback23(channel):
    print("falling edge detected on 23")
    os.system('echo "seek 10" > /home/pi/test_fifo')

def callback27(channel):
    print("button 27")
    os.system('echo "pause" > /home/pi/test_fifo')

def callback22(channel):
    print("button 22")
    os.system('echo "seek -10" > /home/pi/test_fifo')

def callback26(channel):
    print("button 26")
    os.system('echo "seek 30" > /home/pi/test_fifo')

def callback19(channel):
    print("button 19")
    os.system('echo "seek -30" > /home/pi/test_fifo')

def callback17(channel):
    print("button 17, quit")
    os.system('echo "q" > /home/pi/test_fifo')
    GPIO.cleanup()
    quit()

GPIO.add_event_detect(17, GPIO.FALLING, callback=callback17, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=callback23, bouncetime=300)
GPIO.add_event_detect(27, GPIO.FALLING, callback=callback27, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=callback22, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=callback26, bouncetime=300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=callback19, bouncetime=300)

time.sleep(10000000000000000)
