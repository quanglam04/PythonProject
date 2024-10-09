import pygame
import math
import random
from bullet_logic import Bullet_logic


class Bullet_normal(Bullet_logic):
    def __init__(self, x, y, angle):
        self.image = pygame.image.load("asset/bullet.png")
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (15, 15))  # Điều chỉnh kích thước đạn
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = 0.5
        self.length = 15
        self.x = x
        self.y = y
        self.bounces = 0  # Số lần có thể phản xạ (nảy) trước khi biến mất
        self.normal = [0, 0]

        #Tính toán vector hướng dựa theo góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

        self.end_x = 0
        self.end_y = 0

        self.check = False

    def draw(self, window):
        # Cập nhật vị trí đạn dựa trên chuyển động
        self.x += self.direction_x
        self.y += self.direction_y
        self.rect.center = (self.x, self.y)

        # Xoay đạn dựa theo góc và vẽ lên màn hình
        rotated_bullet = pygame.transform.rotate(self.image, -self.angle)
        
        # Tính toán lại vị trí của viên đạn sau khi xoay
        new_rect = rotated_bullet.get_rect(center=self.rect.center)
        
        window.blit(rotated_bullet, new_rect)

    



    