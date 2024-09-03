import pygame
import math

class Bullet:
    def __init__(self, x, y, angle, speed = 2):
        self.image = pygame.image.load("C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 10 ))  # Điều chỉnh kích thước đạn
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = speed
        
        # Tính toán vector hướng dựa trên góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

    def move(self):
        # Cập nhật vị trí của đạn dựa trên hướng đã tính toán
        self.rect.x += self.direction_x
        self.rect.y += self.direction_y

    def draw(self, window):
        rotated_bullet = pygame.transform.rotate(self.image, -self.angle)
        window.blit(rotated_bullet, self.rect)
