import bge
import math

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
trackRay = cont.sensors["trackRay"]
keySens = cont.sensors["keyOn"]
pSKe = scene.objects["playerMesh_ske"]
camCube = scene.objects["player_coll"]
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
        targetTrack(scene.objects["p_cube"], enemy, player['target'])
        player['target'] = True
        player['enemy'] = enemy
        
        

def rotReap():
    player = scene.objects["3rdcam"]
    if player['target']:
        targetTrack(scene.objects["p_cube"], player['enemy'], player["target"])
        #followChar(scene.objects["player_coll"], scene.objects["p_cube"])

def targetTrack(you, enemy, targeting):
    dY = enemy.worldPosition[1]-you.worldPosition[1]
    dX = enemy.worldPosition[0]-you.worldPosition[0]
    dZ = enemy.worldPosition[2]-you.worldPosition[2]
    
    zrot = you.worldOrientation.to_euler()[2]
    yrot = you.worldOrientation.to_euler()[1]
    xrot = you.worldOrientation.to_euler()[0]

    groundhyp = math.sqrt(math.pow(dX,2) + math.pow(dY,2))
    hyp = enemy.getDistanceTo("player_coll")
    desRot = math.asin(dY / groundhyp)
    xDes = math.asin(dZ / hyp)

    if(dX > 0):
        you.applyRotation([0.0,0.0,(desRot-zrot+(math.radians(0)))], False)
        if not targeting:
            camCube.worldOrientation = you.worldOrientation
    else:
        you.applyRotation([0.0,0.0,(-desRot-zrot+(math.radians(180)))], False)
        if not targeting:
            camCube.worldOrientation = you.worldOrientation
#    if(dZ > 0):
#        you.applyRotation([(xDes+xrot+(math.radians(0))),0.0,0.0], False)
#    else:
#        you.applyRotation([(-xDes+xrot+(math.radians(180))),0.0,0.0], False)
            
def followChar(camCube, pCube):
    dif = pCube.worldOrientation - camCube.worldOrientation
    pCube.worldOrientation = pCube.worldOrientation
    camCube.worldOrientation = camCube.worldOrientation + dif 
#def enemyList(playerPos):

for key,status in keySens.events:
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
                if key == bge.events.XKEY:
                    loE = getEnemies()
                    lockTarget(loE[0])
                    
                  
rotReap()