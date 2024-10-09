import pygame
import math

class Bullet_logic:      
  
    def cal_end_point(self, collision_map):
        self.end_x = self.x + self.length * math.cos(math.radians(self.angle))
        self.end_y = self.y - self.length * math.sin(math.radians(self.angle))

        #Xet va cham
        self.check = False
        for i in collision_map:
            line = i.clipline(self.x, self.y, self.end_x, self.end_y)
            if line and (self.x != line[0][0] and self.y != line[0][1]):
                self.end_x = line[0][0]
                self.end_y = line[0][1]

                self.bounces += 1

                self.check = True

                if line[0][0] == i.x:           #Tuong doc ben trai
                    self.normal = [-1, 0]
                elif abs(line[0][0] - i.x - i.width) <= 1.5:
                    self.normal = [1, 0]        #Tuong doc ben phai
                elif line[0][1] == i.y:
                    self.normal = [0, -1]       #Tuong ngang phia tren
                elif abs(line[0][1] - i.y - i.height) <= 1.5:
                    self.normal = [0, 1]        #Tuong ngang phia duoi

                if self.normal[0] != 0:
                    self.angle = 180 - self.angle
                    self.direction_x *= -1
                else:
                    self.angle = 360 - self.angle
                    self.direction_y *= -1

                break

    def update(self):
        if self.check == True: #collision happen
            self.direction_x = math.cos(math.radians(self.angle)) * self.speed
            self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

            self.x = self.end_x + (self.direction_x*10)
            self.y = self.end_y + (self.direction_y*10)
        else:
            self.x += self.direction_x
            self.y += self.direction_y

    def is_expired_bullet(self):
        return self.bounces >= 6