import pygame
import math


class Bullet:
    def __init__(self, x, y, angle, speed=0.2):
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

    def move(self):
        # Cập nhật vị trí của đạn dựa trên hướng đã tính toán
        self.bullet_x += self.direction_x
        self.bullet_y += self.direction_y
        self.rect.x = int (self.bullet_x)
        self.rect.y= int (self.bullet_y)

    def draw(self, window):
        rotated_bullet = pygame.transform.rotate(self.image, -self.angle)
        window.blit(rotated_bullet, self.rect)


    def is_expired_bullet(self):
        return pygame.time.get_ticks()-self.creation_time>4000