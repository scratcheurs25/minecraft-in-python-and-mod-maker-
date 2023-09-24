import pygame

player_img = "player.png"

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(screen,players):
        global player_img
        for player in players:
            screen.blit(pygame.transform.scale(pygame.image.load(player_img),(90,90)),(player.x,player.y))
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