import pygame
import math

class Tank:
    def __init__(self, image_path, window_width, window_height):
        self.tank_image = pygame.image.load(image_path)
        self.tank_rect = self.tank_image.get_rect()
        self.tank_width, self.tank_height = self.tank_rect.size
        self.tank_x = window_width // 2 - self.tank_width // 2
        self.tank_y = window_height // 2 - self.tank_height // 2
        self.tank_angle = 0
        self.tank_speed = 0.2
        # Lưu vị trí cuối cùng không va chạm
        self.last_valid_x = self.tank_x
        self.last_valid_y = self.tank_y
        self.last_valid_angle = self.tank_angle  # Góc quay xe tăng

    def move(self, speed):
        rad_angle = math.radians(self.tank_angle)
        self.tank_x += speed * math.cos(rad_angle)
        self.tank_y -= speed * math.sin(rad_angle)
        self.tank_rect.x = int(self.tank_x)
        self.tank_rect.y = int(self.tank_y)

    def rotate(self, angle):
        self.tank_angle = (self.tank_angle + angle) % 360