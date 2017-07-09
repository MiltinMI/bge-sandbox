import bge
import math


cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
keyboard = cont.sensors["keyOn"]
skelly = scene.objects["playerMesh_ske"]

class Spell(object):
    def __init__(self, ID, startframe, endframe, dmg, mana, spellEff, spellAct):
        self.ID = ID
        self.startframe = startframe
        self.endframe = endframe
        self.dmg = dmg
        self.mana = mana
        self.spellEff = spellEff
        self.spellAct = spellAct
        

crysBall = Spell("Crystal Ball", 1, 68, 5, 3, "shimmer", "crysSpawn")
devFlam = Spell("flameCast", 1, 92, 2, 1, "shimmer", "engulf")

myspells = [crysBall, devFlam]

def spellCast(spell):
    skelly.playAction(spell.ID, spell.startframe, spell.endframe, 1, 0, 1, play_mode = 0, speed = 1)

for key,status in keyboard.events:
    
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_ACTIVE:
                if key == bge.events.BKEY:
                    spellCast(myspells[1])
                    

 

