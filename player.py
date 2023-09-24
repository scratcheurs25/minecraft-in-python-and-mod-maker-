import pygame

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(screen,players):
        for player in players:
            screen.blit(pygame.transform.scale(pygame.image.load("player.png"),(90,90)),(player.x,player.y))
    def v(vx,vy,players):
        for player in players:
            player.x += vx
            player.y += vy
    def playerx(players):
        for player in players:
            return player.x
    def playery(players):
        for player in players:
            return player.y