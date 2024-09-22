import pygame
import Setting
from tank_logic import TankLogic

class TankControl:
    def __init__(self, tank, window_width, window_height):
        self.tank = tank #chuyen tham so cua xe tang vao bao gom kich co vi tri goc quay
        self.window_width = window_width #tham so man hinh game
        self.window_height = window_height

    def handle_input(self):#doc event hay doc input cua pygame
        keys = pygame.key.get_pressed()
        if keys[Setting.up_player_1] :
            TankLogic.move_tank(self.tank, self.tank.tank_speed + float(Setting.speedAdd), self.window_width, self.window_height) #goi den ham di chuyen nha ae
        if keys[Setting.down_player_1]:
            TankLogic.move_tank(self.tank, -self.tank.tank_speed - float(Setting.speedAdd), self.window_width, self.window_height)
        if keys[Setting.right_player_1]:
            TankLogic.rotate_tank(self.tank, Setting.angle)
        if keys[Setting.left_player_1]:
            TankLogic.rotate_tank(self.tank, -Setting.angle)

