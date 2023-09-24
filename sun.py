import pygame

class sun:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(suns,screen):
        for sun in suns:
            pygame.draw.rect(screen,(255,255,0),(sun.x,sun.y,90,90))
