import pygame
import math

class Laser:        #Buoc 2: Đạn laser
    def __init__(self, x, y, angle):
        self.color = (255, 0, 0)  # Màu của tia laser
        self.width = 4  # Độ dày của tia laser
        self.length = 20  # Chiều dài của tia laser
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1.5
        self.creation_time = pygame.time.get_ticks()
        self.bounces = 0  # Số lần có thể phản xạ (nảy) trước khi biến mất
        self.normal = [0, 0]

        #Tính toán vector hướng dựa theo góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

        #Toa do diem cuoi cua dan laser
        self.end_x = 0
        self.end_y = 0

        self.check = False

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

    def draw(self, window):
        pygame.draw.line(window, self.color, [self.x, self.y], [self.end_x, self.end_y], self.width)

    def is_expired_bullet(self):
        # Tia laser hết hiệu lực nếu số lần phản xạ đã hết
        return self.bounces >= 6
