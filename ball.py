import pygame

class Ball:
    def __init__(self,x,y,rad,mass):
        self.x = x
        self.y = y
        self.rad = rad
        self.mass = mass
        self.vy = 0

    def update(self, height):
        self.vy+=0.3
        self.y +=self.vy
        if self.y + self.rad == height:
            self.y = height - self.rad
            self.vy = 0
        elif self.y + self.rad > height:
            print(self.y)
            self.y = height - self.rad
            self.vy = -(self.vy * 0.7)
            print(self.y)
            

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, int(self.y)), self.rad)