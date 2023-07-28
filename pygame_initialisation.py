from manim import *
import pygame

pygame.init()

width = 1600
height = 1200
running = True

# define classes here

scrn = pygame.display.set_mode((width, height))

# define functions here

while running:
    scrn.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()