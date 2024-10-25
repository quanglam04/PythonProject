from bullet import Bullet
class Minigun(Bullet):
    def __init__(self,tank, x, y, angle, speed=1):
        super().__init__(tank, x, y, angle, speed=1)
        self.radius=2
        #self.dame=3
        self.name="Mini"
    def is_expired_bullet(self):
        return self.bounce_count >1
    def dame(self):
        if self.tank.dame_bonus !=0:
            return 5
        return 2