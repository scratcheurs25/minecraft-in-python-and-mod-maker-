import game.block as ModBlock
import game.main as Game


def makeBLocksInWord(block:ModBlock.block):
    Game.blocks.append(block)
class Block(ModBlock.block):
    def __init__(self, id):
        super().__init__(0,0,id)
    def get(self,x,y):
        return ModBlock.block(x,y,self.id)


def dirt(x,y):
    return ModBlock.block(x,y,"game\dirt.png")
def grass(x,y):
    return ModBlock.block(x,y,"game\grass.png")
def stone(x,y):
    return ModBlock.block(x,y,"game\stone.png")
