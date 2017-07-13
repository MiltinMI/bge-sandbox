import bge
import math
#when clicky certain movement key:
#    if rotated correctly do nothing
#    else rotate according to camera rotation ref (player_coli)

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
keyboard = cont.sensors["keyOri"]
orientRef = scene.objects["player_coll"]
player = scene.objects["p_cube"]
playerSke = scene.objects["playerMesh_ske"]
target = scene.objects["3rdcam"]["target"]

def move(movement):
    player.applyMovement(movement, True)
    playerSke.playAction("regRun", 1, 28, 0, 2)

for key,status in keyboard.events:
    if not target:
        # key[0] == bge.events.keycode, key[1] = status
        refRot = orientRef.worldOrientation.to_euler()[2]
        playerRot = player.worldOrientation.to_euler()[2]
        if status == bge.logic.KX_INPUT_ACTIVE:
                if key == bge.events.WKEY:
                    if not (playerRot == refRot):
                        playerRot = (refRot - playerRot)
                        player.applyRotation([0.0,0.0,playerRot], False)
                        orientRef.applyRotation([0.0,0.0,(-playerRot)], False)
                    move([0.05,0.0,0.0])
                    #rotate if not already
                elif key == bge.events.AKEY:
                    refRot = refRot+(math.radians(90))
                    if not (playerRot == (refRot)):
                        playerRot = (refRot - playerRot)
                        player.applyRotation([0.0,0.0,playerRot], False)
                        orientRef.applyRotation([0.0,0.0,(-playerRot)], False)
                    move([0.05,0.0,0.0])
                    #rotate if not already
                elif key == bge.events.DKEY:
                    refRot = refRot-(math.radians(90))
                    if not (playerRot == (refRot)):
                        playerRot = (refRot - playerRot)
                        player.applyRotation([0.0,0.0,playerRot], False)
                        orientRef.applyRotation([0.0,0.0,(-playerRot)], False)
                    move([0.05,0.0,0.0])
                    #rotate if not already
                elif key == bge.events.SKEY:
                    refRot = refRot-(math.radians(180))
                    if not (playerRot == (refRot)):
                        playerRot = (refRot - playerRot)
                        player.applyRotation([0.0,0.0,playerRot], False)
                        orientRef.applyRotation([0.0,0.0,(-playerRot)], False)
                    move([0.05,0.0,0.0])
    elif target:
        if key == bge.events.WKEY:
            move([0.05,0.0,0.0])
        elif key == bge.events.AKEY:
            move([0.0,0.03,0.0])
        elif key == bge.events.DKEY:
            move([0.0,-0.03,0.0])
        elif key == bge.events.SKEY:
            move([-0.03,0.0,0.0])


#worldOrientation.to_euler()