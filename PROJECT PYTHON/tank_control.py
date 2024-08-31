import pygame
from tank_logic import TankLogic

class TankControl:
    def __init__(self, tank, window_width, window_height):
        self.tank = tank #chuyen tham so cua xe tang vao bao gom kich co vi tri goc quay
        self.window_width = window_width #tham so man hinh game
        self.window_height = window_height

    def handle_input(self):#doc event hay doc input cua pygame
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            TankLogic.move_tank(self.tank, self.tank.tank_speed, self.window_width, self.window_height) #goi den ham di chuyen nha ae
        if keys[pygame.K_s]:
            TankLogic.move_tank(self.tank, -self.tank.tank_speed, self.window_width, self.window_height)
        if keys[pygame.K_a]:
            TankLogic.rotate_tank(self.tank, 2.5)
        if keys[pygame.K_d]:
            TankLogic.rotate_tank(self.tank, -2.5)

