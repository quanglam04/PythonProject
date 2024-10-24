import pygame
import Setting
from tank_logic import TankLogic
import math
from bullet import Bullet
from pygame import mixer
from bullet_Lazer import Laser
class TankControl:
    def __init__(self, tank, window_width, window_height,bullets,lasers,control_setting):
        self.tank = tank #chuyen tham so cua xe tang vao bao gom kich co vi tri goc quay
        self.window_width = window_width #tham so man hinh game
        self.window_height = window_height
        self.bullets=bullets
        self.lasers=lasers
        self.last_shoot=0
        self.control_setting=control_setting
        self.bullet_sound = mixer.Sound(Setting.bulletMusic)
        self.bullet_sound.set_volume(0.4)
    def handle_input(self):#doc event hay doc input cua pygame
        keys = pygame.key.get_pressed()
        if keys[self.control_setting['up']] :
            TankLogic.move_tank(self.tank, self.tank.tank_speed + float(self.tank.speed_add), self.window_width, self.window_height) #goi den ham di chuyen nha ae
        if keys[self.control_setting['down']]:
            TankLogic.move_tank(self.tank, -self.tank.tank_speed - float(self.tank.speed_add), self.window_width, self.window_height)
        if keys[self.control_setting['right']]:
            TankLogic.rotate_tank(self.tank, -Setting.angle)
        if keys[self.control_setting['left']]:
            TankLogic.rotate_tank(self.tank, +Setting.angle)
        if keys[self.control_setting['shoot']]:
            if self.tank.gun_mode == 1:
                current_time=pygame.time.get_ticks()
                if  (current_time-self.last_shoot) >500  and len(self.bullets) <5  :
                    bullet = Bullet(self.tank,
                        self.tank.tank_rect.centerx + 29 * math.cos(math.radians(self.tank.tank_angle)),
                        self.tank.tank_rect.centery - 29 * math.sin(math.radians(self.tank.tank_angle)),
                        self.tank.tank_angle)
                    self.bullets.append(bullet)
                    self.last_shoot=current_time
                    self.bullet_sound.play()
            elif self.tank.gun_mode == 2:
                laser=Laser(self.tank,self.tank.tank_rect.centerx + 29 * math.cos(math.radians(self.tank.tank_angle)),
                            self.tank.tank_rect.centery - 29 * math.sin(math.radians(self.tank.tank_angle)),
                            self.tank.tank_angle)
                self.lasers.append(laser)
                self.tank.tank_laser.active =False



