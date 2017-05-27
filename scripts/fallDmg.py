import bge
import aud

#Spaghetti code, will fix.
def main():
    device = aud.device()
    controller = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    obj = controller.owner
    skelly = scene.objects["playerMesh_ske"]
    url = bge.logic.expandPath("//audio\sfx\crack.wav") 
    sound = aud.Factory.file(url)
    sound = sound.pitch(2)
    linVz = obj.getLinearVelocity(True)[2] #gets z-velocity
    fallray = controller.sensors["fallRay"]
    if linVz < (-8) and fallray.positive: #down is negative, fallray checks if player has hit the ground to finalize damage.
        print("You're hit with ",int(linVz*linVz*linVz*(-0.13))," points of falldamage")
        linVz = 0
        device.play(sound)
        url = bge.logic.expandPath("//audio\sfx\dmg_grunt.wav") 
        sound = aud.Factory.file(url)
        device.play(sound)
        skelly.playAction("fallCri", 1, 13, 1, 0, 1, play_mode = 0, speed = 0.6)
main()    
    





