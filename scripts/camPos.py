import bge
import aud

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
keyboard = cont.sensors["keyDist"]
#see blender file for actual placement of these objects.
empty = scene.objects["empty"]
reset = scene.objects["reset"]
print(scene.objects["enemy"])
device = aud.device()
musBox = cont.actuators['mainMus']
url = bge.logic.expandPath("//audio\music\Boss1.mp3") 
sound = aud.Factory(url)
sound = sound.pitch(1)

uDome = scene.objects["upper_dome"]
lDome = scene.objects["lower_ground"]

cam = scene.objects["3rdcam"]
playerPoint = scene.objects["player_coll"]
bossfight = playerPoint['bossfight']
#ray sensor is connected to "fpscam"
ray = cont.sensors["ray"]

for key,status in keyboard.events:
    if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        if key == bge.events.WHEELUPMOUSE or key == bge.events.WHEELDOWNMOUSE:
            calcRange()

def calcRange():
    ray.range = (cam.worldPosition - playerPoint.worldPosition).length
    print(ray.range)

def domeTrack():
    uDome.worldPosition = cam.worldPosition
    lDome.worldPosition = cam.worldPosition
    
#Camera position depending on ray output.
if ray.positive:
    empty.worldPosition = ray.hitPosition
else:
    empty.worldPosition = reset.worldPosition    
    
domeTrack()

z_pos = playerPoint.worldPosition[2]

if z_pos > 17 and not bossfight:
   musBox.stopSound()
   device.volume = 0.5
   device.play(sound)
   playerPoint['bossfight'] = True