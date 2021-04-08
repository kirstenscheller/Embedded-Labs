# ECE5725 Th3:30 Lab
# motor_control.py
# kes334 ih258

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
#pin 6 is AI2
GPIO.setup(6, GPIO.OUT)
#pin 5 is AI1
GPIO.setup(5, GPIO.OUT)

#GPIO.output(6, GPIO.HIGH)


frequency = 50
dc = 0

pwm = GPIO.PWM(13, 10)
pwm.start(dc)
print ("Clockwise, stopped")
time.sleep(3)

pwm.ChangeDutyCycle(50)
print ("Clockwise, half speed")
GPIO.output(6, GPIO.LOW)
GPIO.output(5, GPIO.HIGH)
time.sleep(3.0)


pwm.ChangeDutyCycle(100)
print ("Clockwise, full speed")
time.sleep(3)

pwm.ChangeDutyCycle(0)
print("Counter Clockwise, stopped")
time.sleep(3)

GPIO.output(6, GPIO.HIGH)
GPIO.output(5, GPIO.LOW)

pwm.ChangeDutyCycle(50)
print("Counter Clockwise, half speed")
time.sleep(3)

pwm.ChangeDutyCycle(100)
print("Counterclockwise, full speed")
time.sleep(3)



pwm.stop()
GPIO.cleanup()
