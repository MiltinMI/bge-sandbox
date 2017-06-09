import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
keyboard = cont.sensors["keyDist"]
#see blender file for actual placement of these objects.
empty = scene.objects["empty"]
reset = scene.objects["reset"]

cam = scene.objects["3rdcam"]
playerPoint = scene.objects["player_coll"]
#ray sensor is connected to "fpscam"
ray = cont.sensors["ray"]

for key,status in keyboard.events:
    if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        if key == bge.events.WHEELUPMOUSE or key == bge.events.WHEELDOWNMOUSE:
            calcRange()

def calcRange():
    ray.range = (cam.worldPosition - playerPoint.worldPosition).length
    print(ray.range)
#Camera position depending on ray output.
if ray.positive:
    empty.worldPosition = ray.hitPosition
else:
    empty.worldPosition = reset.worldPosition    