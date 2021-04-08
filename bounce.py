# ECE 5725 Thursday
# kes334 ih258

import pygame
import os
import commands
import RPi.GPIO as GPIO

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

size = width, height = 320,240
speed = [2,2]
black = 0,0,0

screen = pygame.display.set_mode((width, height))
ball = pygame.image.load('Downloads/trophy_ball.png')
ballrect = ball.get_rect()

playing = True

while playing:
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()


    if not GPIO.input(17):
        print (" quitting")
        playing = False

GPIO.cleanup()
