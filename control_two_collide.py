# ECE5725 Th330 Lab
# control_two_collide.py
#kes334 ih258

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

framerate = 30

pygame.init()
size = width, height = 320,240
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(False)
#pygame.mouse.set_visible(True)
BLACK = 0,0,0
WHITE = 255,255,255
#size = width, height = 320,240
font = pygame.font.SysFont('Corbel', 35)
smallfont = pygame.font.SysFont('Corbel', 25)
qtext = font.render('quit', True, WHITE)
stext = font.render('start', True, WHITE)
ptext = font.render('Pause', True, WHITE)
ftext = font.render('Fast', True, WHITE)
slowtext = font.render('Slow', True, WHITE)
btext = font.render('Back', True, WHITE)

hit = ""
coor = font.render(hit, True, WHITE)

clock = pygame.time.Clock()
speed = [7,7]
speed2 = [10,8]
ball = pygame.image.load('Downloads/football.png')
ballrect = ball.get_rect()
ball2 = pygame.image.load('Downloads/ornament.png')
ballrect2 = ball2.get_rect()
ballrect2 = ballrect2.move(width//2, height//2)

bouncing = False
screen1 = True

while loop:
    screen.fill(BLACK)
    if screen1 == False:
        prect = ptext.get_rect()
        prect = prect.move(1,200)
        screen.blit(ptext, prect)
        frect = ftext.get_rect()
        frect = frect.move(100, 200)
        screen.blit(ftext, frect)
        slowrect = slowtext.get_rect()
        slowrect = slowrect.move(180, 200)
        screen.blit(slowtext, slowrect)
        brect = btext.get_rect()
        brect = brect.move(260, 200)
        screen.blit(btext, brect)

        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x,y = pos
                if y > 200:
                    if x < 50:
                        print('Pause')
                        bouncing = not bouncing
                    elif(x > 50 and x < 150):
                        print('Fast')
                        framerate = framerate * 1.25
                    elif (x > 150 and x < 250):
                        print("Slowing down")
                        framerate = framerate * 0.75
                    elif(x > 250):
                        bouncing = False
                        screen1 = True
    
        if(bouncing):
            ballrect = ballrect.move(speed)
            ballrect2 = ballrect2.move(speed2)
            if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                speed[1] = -speed[1]
            if ballrect2.left < 0 or ballrect2.right > width:
                speed2[0] = -speed2[0]
            if ballrect2.top < 0 or ballrect2.bottom > height:
                speed2[1] = -speed2[1]
            if ballrect.colliderect(ballrect2):
                speed[0] = -speed[0]
                speed[1] = -speed[1]
                speed2[0] = speed2[0]
                speed2[1] = -speed2[1]
            screen.blit(ball, ballrect)
            screen.blit(ball2, ballrect2)


    if(screen1):
        qrect = qtext.get_rect()
        qrect = qrect.move(30,200)
        screen.blit(qtext, qrect)
        coor = font.render(hit, True, WHITE)
        coor_rect = coor.get_rect(center=(160,120))
        screen.blit(coor, coor_rect)
        srect = stext.get_rect()
        srect = srect.move(260, 200)
        screen.blit(stext, srect)

        for event in pygame.event.get():
            if (event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x,y = pos
                if y > 200:
                    if x < 100:
                        print("Exit Buuttoonn!!")
                        loop = False
                    elif x > 230:
                        print("Starting the bouncing")
                        bouncing = True
                        screen1 = False
                else:
                    # the hit coordinates stuff
                    print("Hit: " + str(x) + ', ' + str(y))
                    hit = str(x) + ', ' + str(y)
                    #coor = font.render(hit, True, WHITE)
                    #coor_rect = coor.get_rect(center=(100,100))
                    #screen.blit(coor, coor_rect)
    pygame.display.flip()
    clock.tick(framerate)
    if not GPIO.input(17):
        loop = False


