# ECE5725 Th3:30 Lab
# blink.py
# kes334 ih258

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#make GPIO 13 output
GPIO.setup(13, GPIO.OUT)

#quit button?
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#pwm parameters:
frequency = 1
dc = 5.0 
#PWM
pwm = GPIO.PWM(13, frequency)
pwm.start(dc)


#have 17 as quit button
while GPIO.input(17):
    pass

pwm.stop()
GPIO.cleanup()
