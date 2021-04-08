# ECE5725 TH330 Lab
# run_test.py
# kes334 ih258

#this function operates by using the on-pi buttons. Each one has a command: stop, clockwise, counterclockwise, or stop. PUshing the buttons creates an event which goes to a certain function. In this function, the parameters are determined and sent to a function called motor_pls. Motor_pls takes in the wheel being controlled and the command to be send and sends the propoer GPIO commands to achieve this.

import os
import sys
import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#start time
start_time = time.time()

#output motor control buttons
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

#input contrl buttons
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#set servos, no move
rs = GPIO.PWM(13, 50)
rs.start(0)
ls = GPIO.PWM(4, 50)
ls.start(0)

#Initilize all piTFT drivers
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

#Initialize screen and text
pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode((width,height))
pygame.mouse.set_visible(False)
BLACK = 0,0,0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
font = pygame.font.SysFont('Corbel', 25)
font_hist = pygame.font.SysFont('Corbel', 15)
qtext = font.render('QUIT', True, WHITE)
rtext = font.render('RESUME', True, WHITE)
stext = font.render('STOP', True, WHITE)
starttext= font.render('START', True, WHITE)
rightHist = font_hist.render('Right History', True, WHITE)
rightArr = ["none", "none", "none"]
leftHist = font_hist.render('Left History', True, WHITE)
leftArr = ["none", "none", "none"]


def motor_pls(s, direction):
    #This function changes the direction of the desired servo (denoted by s)
    if direction == "stop":# stop the wheel
        if s == "right":
            rs.ChangeDutyCycle(0)
            rightArr.append("stop     " + str(time.time()-start_time) )
            rightArr.pop(0)
        elif s == "left":
            ls.ChangeDutyCycle(0)
            leftArr.append("stop   " + str(time.time() - start_time))
            leftArr.pop(0)
    elif direction == "cw":
        if s == "right":
            GPIO.output(5, GPIO.HIGH) # these are the pin settings for clockwise direction
            GPIO.output(6, GPIO.LOW)
            rs.ChangeDutyCycle(75)
            rightArr.append("cw   " + str(time.time()-start_time))
            rightArr.pop(0)
        elif s == "left": # clockwise
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            ls.ChangeDutyCycle(75)
            leftArr.append("cw   " + str(time.time() - start_time))
            leftArr.pop(0)
    elif direction == "ccw": # counterclockwise
        if s == "right":
            GPIO.output(5, GPIO.LOW) # opposite GPIO high and low to make direction change
            GPIO.output(6, GPIO.HIGH)
            rs.ChangeDutyCycle(75)
            rightArr.append("ccw   " + str(time.time() - start_time))
            rightArr.pop(0)
        elif s == "left":
            GPIO.output(26, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            ls.ChangeDutyCycle(75)
            leftArr.append("ccw   " + str(time.time() - start_time))
            leftArr.pop(0)

right = True

def stop(channel):
    print ("stopping")
    if right:
        motor_pls("right", "stop") # stop the right wheel by calling motor_pls on wheel "right" with command "stop"
    else:
        motor_pls("left" , "stop") # stop the left wheel by calling motor_pls on wheel "left" with command "Stop"

def cw(channel):
    print ("Cw")
    if right:
        motor_pls("right" , "cw") 
    else:
        motor_pls("left", "cw")

def ccw(channel):
    print ("ccw")
    if right:
        motor_pls("right", "ccw")
    else:
        motor_pls("left", "ccw")

def switch_wheel(channel):
    print ("switching wheel")
    global right # change global wheel direction so later commands are now for the opposite wheel
    right = not right


#button detectors - create an event for each button which calls the specific command from above
GPIO.add_event_detect(27, GPIO.FALLING, callback = stop, bouncetime= 200)
GPIO.add_event_detect(23, GPIO.FALLING, callback = cw, bouncetime = 200)
GPIO.add_event_detect(22, GPIO.FALLING, callback = ccw, bouncetime = 200)
GPIO.add_event_detect(17, GPIO.FALLING, callback = switch_wheel, bouncetime = 200)


# important varaibles for running
running = True
isGo = True # a state for the screen we are currently on (isGo means we are on the running screen)
            # isGo = false means the panic stop has been pressed
last_state = ["left", "stop", "right", "stop"]
first = True
started_state = False
#state machine: 0-7 are Forward, STop, Backwards, STop, Left, Stop, Pivot Right, Stop
state = 0
time_state = 0
started = False


#run loop to display everything on the pi and run thetest
while running:
    screen.fill(BLACK)
    
    #render the panic button
    if isGo: # if isGo then we are in run stage and button should be red and read "quit"
        pygame.draw.circle(screen, RED, (220, 200), 40)
        stext_rect = stext.get_rect()
        stext_rect = stext_rect.move(200,200)
        screen.blit(stext, stext_rect)
    else:
        pygame.draw.circle(screen, GREEN, (220, 200), 40)
        rtext_rect = rtext.get_rect()
        rtext_rect = rtext_rect.move(200, 200)
        screen.blit(rtext, rtext_rect)
    
    #render quit and start button upper right
    qtext_rect = qtext.get_rect()
    qtext_rect = qtext_rect.move(225, 20)
    screen.blit(qtext, qtext_rect)
    starttext_rect = starttext.get_rect()
    starttext_rect = starttext_rect.move(225, 100)
    screen.blit(starttext, starttext_rect)

    #render the histories - left
    leftHist_rect = leftHist.get_rect()
    leftHist_rect = leftHist_rect.move(1, 10)
    screen.blit(leftHist, leftHist_rect)
    left1_text = font.render(leftArr[0], True, WHITE)
    left1_rect = left1_text.get_rect()
    left1_rect = left1_rect.move(20, 20)
    screen.blit(left1_text, left1_rect)
    left2_text = font.render(leftArr[1], True, WHITE)
    left2_rect = left2_text.get_rect()
    left2_rect = left2_rect.move(20, 40)
    screen.blit(left2_text, left2_rect)
    left3_text = font.render(leftArr[2], True, WHITE)
    left3_rect = left3_text.get_rect()
    left3_rect = left3_rect.move(20, 60)
    screen.blit(left3_text, left3_rect)
    #render the histories - right
    rightHist_rect = rightHist.get_rect()
    rightHist_rect = rightHist_rect.move(1, 100)
    screen.blit(rightHist, rightHist_rect)
    right1_text = font.render(rightArr[0], True, WHITE)
    right1_rect = right1_text.get_rect()
    right1_rect = right1_rect.move(20, 120)
    screen.blit(right1_text, right1_rect)
    right2_text = font.render(rightArr[1], True, WHITE)
    right2_rect = right2_text.get_rect()
    right2_rect = right2_rect.move(20, 140)
    screen.blit(right2_text, right2_rect)
    right3_text = font.render(rightArr[2], True, WHITE)
    right3_rect = right3_text.get_rect()
    right3_rect = right3_rect.move(20, 160)
    screen.blit(right3_text, right3_rect)

    #Run_Test - STATE MACHINE
    if started: # aka if the panic button not been pressed
        if state == 0:
            if first:
                first = False
                time_state = time.time()
            elif (time.time()-time_state >= 3.0):
                state = 1
                motor_pls("right", "stop")
                motor_pls("left", "stop")
                time_state = time.time()
                started_state = False
            elif started_state == False:
                print ("going forward")
                motor_pls("right", "cw")
                motor_pls("left", "cw")
                started_state = True
        elif state == 1 or state ==3 or state==5 or state==7: # all the stops
            if (time.time() - time_state >= 1.5):
                if state == 7:
                    state = 0 # reached end, go back to beginning to repeat
                else:
                    state = state + 1
                    print (state)
                started_state = False
                time_state = time.time()
            elif started_state == False:
                print (" in stopped state")
                started_state = True
        elif state == 2:
            if (time.time() - time_state >=3):
                state = 3
                motor_pls("left", "stop")
                motor_pls("right", "stop")
                time_state = time.time()
                started_state = False
            elif started_state == False:
                motor_pls("right", "ccw")
                motor_pls("left", "ccw")
                started_state = True
                print ("going backwards - state 2")
        elif state == 4:
            if (time.time() - time_state >=1):
                state = 5
                motor_pls("left", "stop")
                motor_pls("right", "stop")
                time_state = time.time()
                started_state = False
            elif started_state == False:
                motor_pls("right", "ccw")
                motor_pls("left", "cw")
                print ("pivoting left")
                started_state = True
        elif state ==6:
            if (time.time() - time_state >=1):
                state = 7
                motor_pls("right", "stop")
                motor_pls("left", "stop")
                time_state = time.time()
                started_state = False
            elif started_state == False:
                motor_pls("right", "cw")
                motor_pls("left", "ccw")
                started_state = True
                print ("pivoting right")




    #monitor for piTFT touches
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if (x>200) and (y<50):
                print ("Quitting")
                running = False
            if (x>200) and (y>50 and y<150): #start button pressed
                started = True
                isGo = True
            if (x>150) and (y>150):
                print ("resume/play")
                if isGo:
                    if "ccw" in leftArr[2]:
                        last_state[1] = "ccw"
                    elif "cw" in leftArr[2]:
                        last_state[1] = "cw"
                    elif "stop" in leftArr[2]:
                        last_state[1] = "stop"

                    if "ccw" in rightArr[2]:
                        last_state[3] = "ccw"
                    elif "cw" in rightArr[2]:
                        last_state[3] = "cw"
                    elif "stop" in rightArr[2]:
                        last_state[3] = "stop"

                    started = False
                    motor_pls("right", "stop")
                    motor_pls("left", "stop")
                else:
                    motor_pls(last_state[0], last_state[1])
                    motor_pls(last_state[2], last_state[3])
                isGo = not isGo

    


    pygame.display.flip()


GPIO.cleanup()
rs.stop()
ls.stop()
quit()
