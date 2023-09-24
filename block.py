import pygame

class block:
    def __init__(self,x,y,id):
        self.x = x
        self.y = y
        self.id = id
    def draw(blocks,screen):
        for block in blocks:
            screen.blit(pygame.transform.scale(pygame.image.load(block.id),(90,90)),(block.x,block.y))
    def collider(blocks,rectx,recty):
        for block in blocks:
            if block.x < rectx  + 90 and rectx < block.x + 90 and block.y < recty + 90 and recty < block.y + 90:
                return True
