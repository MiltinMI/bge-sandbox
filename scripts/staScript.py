import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
scenes = bge.logic.getSceneList()
for scene in scenes:
    if scene.name == "Main":
        rollStatus = scene.objects['playerMesh_ske']['roll']
def refresh(max, cur, status):
    if not status:
        cur += 1
    if cur < max:
        return cur
    else:
        return max

mpBar = scene.objects['mp']
maxMp = mpBar['maxStamina']
mp = mpBar['stamina']
mpBar['stamina'] = refresh(maxMp, mp, rollStatus)
scene.objects['mp_back']['backdrop'] = maxMp