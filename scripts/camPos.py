import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
#see blender file for actual placement of these objects.
empty = scene.objects["empty"]
reset = scene.objects["reset"]
#ray sensor is connected to "fpscam"
ray = cont.sensors["ray"]
#Camera position depending on ray output.
if ray.positive:
    empty.worldPosition = ray.hitPosition
else:
    empty.worldPosition = empty.worldPosition    