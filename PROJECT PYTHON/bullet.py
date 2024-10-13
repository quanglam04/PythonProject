import pygame
import math
from bullet_logic import Bullet_logic


class Bullet(Bullet_logic):
    def __init__(self, x, y, angle, speed=0.5   ):
        self.image = pygame.image.load("asset/bullet.png")
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(self.image, (15, 15))  # Điều chỉnh kích thước đạn
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = speed
        self.bullet_x=self.rect.x
        self.bullet_y=self.rect.y
        self.creation_time=pygame.time.get_ticks()

        # Tính toán vector hướng dựa trên góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed
        self.check = 0

    def draw(self, window):
        # Xoay đạn dựa theo góc và vẽ lên màn hình
        rotated_bullet = pygame.transform.rotate(self.image, -self.angle)

        # Tính toán lại vị trí của viên đạn sau khi xoay
        new_rect = rotated_bullet.get_rect(center=self.rect.center)

        window.blit(rotated_bullet, new_rect)