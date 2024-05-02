import pygame
import random

pygame.init()

SCREEN_WIDTH = 800  #screen size
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #set screen size

pygame.display.set_caption("Game Target")     #screen name
icon = pygame.image.load("img/target.jpg")    #screen image
pygame.display.set_icon(icon)                 #set icon

target_img = pygame.image.load("img/")
target_width = 50
target_height = 50



running = True
while running:
    pass

pygame.quit()