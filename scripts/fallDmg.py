import bge
import aud

#Spaghetti code, will fix.
def checkHP(amount):
    if amount < 1:
        skelly.playAction("deathAnim", 1, 9, 1, 0, 1, play_mode = 0, speed = 0.6)
        print("You DIED")
        
def main():
   
    # to load the scene
    #find the scene and object
    
    url = bge.logic.expandPath("//audio\sfx\crack.wav") 
    sound = aud.Factory.file(url)
    sound = sound.pitch(2)
    linVz = obj.getLinearVelocity(True)[2] #gets z-velocity
    fallray = controller.sensors["fallRay"]
    if linVz < (-8) and fallray.positive: #down is negative, fallray checks if player has hit the ground to finalize damage.
        dmg = int(linVz*linVz*linVz*(-0.13))
        print("You're hit with ",dmg," points of falldamage")
        linVz = 0
        device.play(sound)
        url = bge.logic.expandPath("//audio\sfx\dmg_grunt.wav") 
        sound = aud.Factory.file(url)
        device.play(sound)
        skelly.playAction("fallCri", 1, 13, 1, 0, 1, play_mode = 0, speed = 0.6)
        player['HP'] += -dmg
        percOff = (int(dmg/maxHp*100))
        hp['percent'] += -percOff
        checkHP(player['HP'])
    
        
def drainSta():
    mp['stamina'] += -30
    getSta(mp['stamina'])
    
def getSta(sta):
    player['Sta'] = sta
device = aud.device()
controller = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
obj = controller.owner
keyboard = controller.sensors['keyOn']
scenes = bge.logic.getSceneList()
player = scene.objects['player']
player_hp = player['HP']
maxHp = player['maxHp']
player_sta = player["Sta"]
skelly = scene.objects["playerMesh_ske"]
for scene in scenes :
            if scene.name == 'Stats':
                hp = scene.objects['health']
                mp = scene.objects['mp']
                getSta(mp['stamina']) #for some reason, Blender will claim that mp isn't defined (but still work properly) if placed anywhere else than here.
main()    

for key,status in keyboard.events:
    if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        if key == bge.events.CKEY and player_sta >= 30:
            print(skelly.worldPosition)
            drainSta()
            




