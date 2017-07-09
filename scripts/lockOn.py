import bge
import math

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
trackRay = cont.sensors["trackRay"]
keySens = cont.sensors["keyOn"]
#if target:
#    camTrack()

def getEnemies():
    print("getting enemylist")
    enemyList = []
    for objects in scene.objects:
                        if "enemy" in objects.name and (objects.getDistanceTo("3rdcam") < 10):
                            enemyList.append(objects)
    return enemyList

def lockTarget(enemy): #A keyevent will trigger this function
    player = scene.objects["3rdcam"]
    if player['target']:
        player['target'] = False
        player['enemy'] = "nothing"
    else:
        player['target'] = True
        player['enemy'] = enemy
        targetTrack(scene.objects["player_coll"], enemy)
        

def rotReap():
    player = scene.objects["3rdcam"]
    if player['target']:
        targetTrack(scene.objects["player_coll"], player['enemy'])

def targetTrack(you, enemy):
    dY = enemy.worldPosition[1]-you.worldPosition[1]
    dX = enemy.worldPosition[0]-you.worldPosition[0]
    
    zrot = you.worldOrientation.to_euler()[2]

    hyp = enemy.getDistanceTo("player_coll")
    desRot = math.asin(dY / hyp)

    if(dX > 0):
        you.applyRotation([0.0,0.0,(desRot-zrot+(math.radians(0)))], False)
    else:
        you.applyRotation([0.0,0.0,(-desRot-zrot+(math.radians(180)))], False)


#def enemyList(playerPos):

for key,status in keySens.events:
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
                if key == bge.events.XKEY:
                    loE = getEnemies()
                    lockTarget(loE[0])
                    
                  
rotReap()