import game.block as ModBlock
import game.main as Game


def makeBLocksInWord(block:ModBlock.block):
    Game.blocks.append(block)


def dirt(x,y):
    return ModBlock.block(x,y,"game\dirt.png")
def grass(x,y):
    return ModBlock.block(x,y,"game\grass.png")
def stone(x,y):
    return ModBlock.block(x,y,"game\stone.png")
