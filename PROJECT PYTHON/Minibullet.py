from bullet import Bullet
class Minigun(Bullet):
    def __init__(self,tank, x, y, angle, speed=1):
        super().__init__(tank, x, y, angle, speed=1)
        self.radius=1
    def is_expired_bullet(self):
        return self.bounce_count >1