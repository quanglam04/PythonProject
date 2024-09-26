import math
import pygame
from bullet import Bullet


class BulletStorm:
    def __init__(self, x, y, angle):
        self.bullets = []

        # angle là góc ban đầu bắn
        for i in range(10):
            spread_angle = angle + (i - 5) * 2  # Điều chỉnh góc phát tán
            bullet = Bullet(x, y, spread_angle)
            self.bullets.append(bullet)

    def move(self, map_data,tile_size):
        for bullet in self.bullets[:]:
            bullet.move(map_data, tile_size)
            if bullet.is_expired_bullet():
                self.bullets.remove(bullet)

    def draw(self, window):
        for bullet in self.bullets:
            bullet.draw(window)