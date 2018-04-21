# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
 
SCREEN_SIZE = (640, 480)  # Дэлгэцийн хэмжээ
 
# Pygame-г 
pygame.init()
# SCREEN_SIZE дэлгэц үүсгэх
screen = pygame.display.set_mode(SCREEN_SIZE)
# Гарчиг
pygame.display.set_caption(u"Дэлгэц хийх")
 
# Тоглоомийн тойрог
while True:
    screen.fill((0,0,255))   # Хөх өнгөөр будах
    pygame.display.update()  # дэлгэц шинэчлэх
    # эвент
    for event in pygame.event.get():
        if event.type == QUIT:  # эвент дуусгах
            sys.exit()