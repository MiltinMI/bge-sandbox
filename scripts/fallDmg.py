import bge
controller = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
obj = controller.owner
linVz = obj.getLinearVelocity(True)[2] #gets z-velocity

if linVz < (-10): #down is negative
    print("You're hit with ",int(linVz*linVz*2)," points of falldamage")
