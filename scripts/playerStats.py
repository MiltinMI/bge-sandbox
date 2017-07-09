import bge

class Body(object):
    def __init__(self, hp, mp, dmg):
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        
    def restore(hp, amount):
        return (hp + amount)
    
you = Body(320, 85, 10)