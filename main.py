import numpy
import pygame
from pygame import font
from ball import Ball

gravity = 0.5
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True

bolinhas  = []


while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                nova = Ball(x,y,rad=10,mass=1)
                bolinhas.append(nova)

    for bola in bolinhas:
        bola.draw(screen)

    for bola in bolinhas:
        bola.update(height=480)



    flips = pygame.display.flip()
    clock.tick(60)

pygame.quit