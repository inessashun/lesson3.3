import pygame
import random

pygame.init()

SCREEN_WIDTH = 800  #screen size
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #set screen size

pygame.display.set_caption("Game Target")     #screen name
icon = pygame.image.load("img/аватар.jpg")    #screen image
pygame.display.set_icon(icon)                 #set icon

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    pass

pygame.quit()