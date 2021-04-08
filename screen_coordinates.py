import pygame
import RPi.GPIO as GPIO
import os
import sys
from pygame.locals import *

loop = True
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
#pygame.mouse.set_visible(True)
BLACK = 0,0,0
WHITE = 255,255,255
#size = width, height = 320,240
font = pygame.font.SysFont('Corbel', 35)
qtext = font.render('quit', True, WHITE)
hit = ""
coor = font.render(hit, True, WHITE)

#screen = pygame.display.set_mode((width, height))

qbutton = {'quit':(70,150)}

while loop:
    screen.fill(BLACK)
    qrect = qtext.get_rect()
    qrect = qrect.move(30,200)
    screen.blit(qtext, qrect)
    coor = font.render(hit, True, WHITE)
    coor_rect = coor.get_rect(center=(100,100))
    screen.blit(coor, coor_rect)
    
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 200:
                if x < 100:
                    print("Buuttoonn!!")
                    loop = False
            else:
                # the hit coordinates stuff
                print("Hit: " + str(x) + ', ' + str(y))
                hit = str(x) + ', ' + str(y)
                #coor = font.render(hit, True, WHITE)
                #coor_rect = coor.get_rect(center=(100,100))
                #screen.blit(coor, coor_rect)
    pygame.display.flip()
    if not GPIO.input(17):
        loop = False


