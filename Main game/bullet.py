import pygame
import math
from tank_logic import TankLogic
from Setting import bullet_speed
class Bullet:
    def __init__(self,tank, x, y, angle, speed=bullet_speed):
        self.tank=tank
        self.radius = 5  # Ban kinh cua hinh tron
        self.color = tank.bullet_color
        self.name="Normal"
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.angle = angle #goc ban de tinh ra vector van toc
        self.speed = speed
        self.bullet_x = self.rect.x
        self.bullet_y = self.rect.y
        self.creation_time = pygame.time.get_ticks()
        self.bounce_count = 0  #so lan cham tuong
        #self.dame=10
        # tinh vector van toc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

    def move(self, map_data, tile_size):
        a=self.rect.x+self.radius
        b=self.rect.y+self.radius

        # Canh ben trai
        if map_data[int(b/16)][int ((a+self.radius)/16)]=='1':
            self.direction_x *=-1
            self.bounce_count +=1
        #Canh tren
        elif map_data[int ((b-self.radius)/16)][int(a/16)]=='1':
            self.direction_y *=-1
            self.bounce_count +=1
        #canh duoi
        elif map_data[int ((b+self.radius)/16)][int (a/16)]=='1':
            self.direction_y *=-1
            self.bounce_count+=1
        #canh ben phai
        elif map_data[int (b/16)][int ((a-self.radius)/16)]=='1':
            self.direction_x *=-1
            self.bounce_count+=1
        elif map_data[int((b+self.radius)/16)][int((a+self.radius)/16)]=='1':
            x= int((a+self.radius)/16)*16
            y= int((b+self.radius)/16)*16
            if TankLogic.check_in_circle((x,y),a,b,self.radius):
                if self.direction_x>0:
                    self.direction_x *=-1
                else: self.direction_y *=-1
        elif map_data[int((b - self.radius) / 16)][int((a + self.radius) / 16)] == '1':
            x= int((a+self.radius)/16)*16
            y=int((b - self.radius) / 16)+16
            if TankLogic.check_in_circle((x,y),a,b,self.radius):
                if self.direction_y <0:
                    self.direction_y*=-1
                else: self.direction_x *=-1
        elif map_data[int((b - self.radius) / 16)][int((a - self.radius) / 16)] == '1':
            x=int((a - self.radius) / 16)+16
            y=int((b - self.radius) / 16)
            if TankLogic.check_in_circle((x,y),a,b,self.radius):
                if self.direction_y >0:
                    self.direction_y *=-1
                else: self.direction_x*=-1
        elif map_data[int((b + self.radius) / 16)][int((a - self.radius) / 16)] == '1':
            x=int((a - self.radius) / 16)+16
            y=int((b + self.radius) / 16) +16
            if TankLogic.check_in_circle((x,y),a,b,self.radius):
                if self.direction_x <0:
                    self.direction_x*=-1
                else: self.direction_y *=-1


        # Update bullet position
        self.bullet_x += self.direction_x
        self.bullet_y += self.direction_y
        self.rect.x = int(self.bullet_x)
        self.rect.y = int(self.bullet_y)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)

    def is_expired_bullet(self):
        return self.bounce_count >= 10
    def dame(self):
        if self.tank.dame_bonus != 0:
            return 20
        return 10