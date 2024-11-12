from bullet import Bullet
class ShotGun(Bullet):
    def __init__(self,tank,x,y,angle,speed=1):
        super().__init__(tank,x,y,angle,speed)
        self.radius = 1
        self.name="Shotgun"
    def is_expired_bullet(self):
        return self.bounce_count >2
    def dame(self):
        if self.tank.dame_bonus !=0:
            return 6
        else:
            return 4
