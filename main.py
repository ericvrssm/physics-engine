import numpy
import pygame
from ball import Ball

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                nova = Ball(x,y,rad=100,mass=1)
                bolinhas.append(nova)
    for bola in bolinhas:
        pygame.draw.circle(screen, (0, 0, 0), (bola.x, bola.y), bola.rad)

    pygame.display.flip()
    clock.tick(60)




pygame.quit