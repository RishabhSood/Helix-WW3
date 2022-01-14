# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:02:57 2020

@author: soodr
"""

# World War 3
# A concept by Rishabh Sood and Ishan Malhotra
# Coded by Rishabh Sood
# Storyline by Mihir, Rajat and Tushar
# A MadLads Production

import pygame
from function_lib import userinfo

#----------------------------------------------------------------------------------------------------------#
#Game opening screen
# initialize game engine

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

window_width=925
window_height=577

animation_increment=10
clock_tick_rate=20
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("World War 3")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("trump.png").convert()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

# running the welcome screen
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    largeText = pygame.font.Font('thefont.ttf',55)
    TextSurf, TextRect = text_objects("World War 3", largeText)
    TextRect.center = ((670),(70))
    screen.blit(TextSurf, TextRect)
    button("ATTACK!",620,140,110,50,red,bright_red,userinfo)
    pygame.display.flip()
    clock.tick(clock_tick_rate)
