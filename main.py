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
    screen.fill(color)
    for event in pygame.event.get():             #check actions with cycle -> for
        if event.type == pygame.QUIT:            #save in event and end
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  #event type key down
            mouse_x, mouse_y = pygame.mouse.get_pos()   #mouse click position
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:   #targeting point
                target_x = random.randint(0, SCREEN_WIDTH - target_width)   #random target right_left side
                target_y = random.randint(0, SCREEN_HEIGHT - target_height) #random target up_down side
    screen.blit(target_img, (target_x, target_y))    #image on screen
    pygame.display.update()     #refresh the screen


pygame.quit()