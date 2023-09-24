import pygame
from game.block import block
from game.player import player
from game.sun import sun

pygame.init()

screen = pygame.display.set_mode((800,600))

img = "game\dirt.png"

run = True

jump = 0

move = 0

gravity = True

blocks = []

for x in range(5):
    for y in range(2):
        if y == 0:
            img = "game\grass.png"
        else:
            img = "game\dirt.png"
        y += 5
        blocks.append(block(x * 90,y * 90,img))
for x in range(2):
    x += 7
    for y in range(2):
        if y == 0:
            img = "game\grass.png"
        else:
            img = "game\dirt.png"
        y += 5
        blocks.append(block(x * 90,y * 90,img))
for x in range(1):
    x += 8
    for y in range(1):
        img = "game\stone.png"
        y += 4
        blocks.append(block(x * 90,y * 90,img))
players = []
players.append(player(0,0))

suns = []

suns.append(sun(500,90))

def moveplayer():
    player.v(move,0,players)
def runing():
 global gravity
 global move
 global jump
 global run
 while run:
    screen.fill((0,255,255))
    if not block.collider(blocks,player.playerx(players),player.playery(players)):
        player.v(0,1,players)
    if block.collider(blocks,player.playerx(players),player.playery(players)):
        if gravity:
            player.v(0,-1,players)
        elif jump == 0:
            player.v(0,-1,players)
            if block.collider(blocks,player.playerx(players),player.playery(players)):
                move=0
                player.v(1,1,players)
                if block.collider(blocks,player.playerx(players),player.playery(players)):
                    player.v(-2,0,players)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                move = 1
                gravity = False
            if events.key == pygame.K_LEFT:
                move = -1
                gravity = False
            if events.key == pygame.K_SPACE:
                player.v(0,1,players)
                if block.collider(blocks,player.playerx(players),player.playery(players)):
                    jump = -20
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
                move = 0
    if jump < 0:
        jump += 1
    moveplayer()
    player.v(0,jump,players)
    block.draw(blocks,screen)
    player.draw(screen,players)
    sun.draw(suns,screen)
    pygame.display.update()

