import bge
import math
import aud
import random

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
device = aud.device()

player = scene.objects["p_cube"]
boss = scene.objects["bossenemy_physCube"]
bossSke = scene.objects["boss_ske"]

dist = boss.getDistanceTo(player)

def getState(boss, player):
    boss["state"] = 0

def bossTurn(enemy):
    enemy["track"] = True
    print("turning")
    
    #turn boss around

def bossWalk(skeleton, boss, endframe):
    boss["track"] = True
    skeleton.playAction("bossWalk", 1, endframe, 0)
    boss["endframe"] = endframe
    skeleton["animated"] = True
        
    


if not bossSke["animated"]:
    boss["track"] = True
    if dist < 5:
        bossSke.playAction("nearAttack", 1, 78, 0)
        boss["endframe"] = 78
        bossSke["animated"] = True
        boss["track"] = False
    elif dist < 10:
        bossSke.playAction("regAttack", 1, 81, 0)
        boss["endframe"] = 81
        bossSke["animated"] = True
        boss["track"] = False
    else:
        bossWalk(bossSke, boss, 37)
     

    
if bossSke.isPlayingAction:    
    frame = (int)(bossSke.getActionFrame(0))
    animName = bossSke.getActionName(0)

    if animName == "bossWalk" and frame == boss["endframe"]:
        bossSke["animated"] = False
    elif frame == 16:
        print("BOOM")
        bossSke.setActionFrame(17.5)
        url = bge.logic.expandPath("//audio\sfx\exp_hit.wav") 
        sound = aud.Factory.file(url)
        sound = sound.pitch(2)
        device.play(sound)
    elif frame == boss["endframe"]:
        print("animation done")
        bossSke["animated"] = False
        bossWalk(bossSke, boss, 37)
 