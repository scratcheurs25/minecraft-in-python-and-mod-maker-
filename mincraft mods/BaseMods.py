import LibsMod.BLocks as Blocks
import LibsMod.CustomeName as Name
import LibsMod.PlayerCustom as Player

Blocks.makeBLocksInWord(Blocks.grass(0,100))
Blocks.makeBLocksInWord(Blocks.dirt(0,190))
Blocks.makeBLocksInWord(Blocks.stone(0,280))
Player.change_texture("LibsMod\player.png")
Name.change_name("BaseModName")
