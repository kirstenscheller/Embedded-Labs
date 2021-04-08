# ECE5625 Th330 Lab
# quit_button.py
#kes334 ih258

import pygame
import RPi.GPIO as GPIO
import os
import sys
from pygame.locals import *


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


pygame.init()
size = width, height = 320,240
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(False)
BLACK = 0,0,0
WHITE = 255,255,255
#size = width, height = 320,240
font = pygame.font.SysFont('Corbel', 35)
qtext = font.render('quit', True, WHITE)

#screen = pygame.display.set_mode((width, height))

qbutton = {'quit':(70,150)}

playing = True

while playing:
    screen.fill(BLACK)
    qrect = qtext.get_rect()
    qrect = qrect.move(30,200)
    screen.blit(qtext, qrect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 200:
                if x < 100:
                    print("Button press")
                    playing  = False
    if not GPIO.input(17):
        playing = False

GPIO.cleanup()
