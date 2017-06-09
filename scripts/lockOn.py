import bge


cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
trackRay = cont.sensors["trackRay"]
keySens = cont.sensors["keyOn"]
#if target:
#    camTrack()

for key,status in keySens.events:
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
                if key == bge.events.XKEY and trackRay.positive:
                    objDet = trackRay.hitObject #will only trigger if a specific key_event occurs
                    print(objDet)

def lockTarget(enemy): #A keyevent will trigger this function
    if enemy in enemyList:
        target = True
    else:
        target = False
        
