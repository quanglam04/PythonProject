import pygame
import math
from tank import Tank

class Player:
    def __init__(self, image_path, window_width, window_height, pos_x, pos_y, controls, id_player):
        self.tank = Tank(image_path, window_width, window_height)
        self.tank.tank_x = pos_x
        self.tank.tank_y = pos_y
        #vị trí cuối cùng không va chạm
        self.last_valid_x = pos_x
        self.last_valid_y = pos_y
        self.last_valid_angle = self.tank.tank_angle
        self.id = id_player
        self.controls = controls
        self.health = 100
        self.score = 0
        self.health_bar_width = 40
        self.health_bar_height = 5

    def handle_input(self, keys):
        if keys[self.controls['up']]:
            self.tank.move(self.tank.tank_speed)
        if keys[self.controls['down']]:
            self.tank.move(-self.tank.tank_speed)
        if keys[self.controls['left']]:
            self.tank.rotate(0.25)
        if keys[self.controls['right']]:
            self.tank.rotate(-0.25)

    def draw(self, window):
        rotated_tank = pygame.transform.rotate(self.tank.tank_image, self.tank.tank_angle)
        new_rect = rotated_tank.get_rect(center=self.tank.tank_rect.center)
        window.blit(rotated_tank, new_rect)

    def draw_health_bar(self, window):
        # Tạo hình ảnh thanh máu
        health_bar_surface = pygame.Surface((self.health_bar_width, self.health_bar_height))
        health_bar_surface.set_colorkey((0, 0, 0))  # đặt màu đen là màu trong suốt
        health_bar_surface.fill((255, 0, 0))  # Màu đỏ cho thanh máu
        pygame.draw.rect(health_bar_surface, (0, 255, 0),
            (0, 0, int(self.health_bar_width * (self.health / 100)), self.health_bar_height))

        # Xoay thanh máu theo xe tank
        rotated_health_bar = pygame.transform.rotate(health_bar_surface, self.tank.tank_angle)

        offset_x = -2
        offset_y = -self.tank.tank_rect.height // 2 - 10

        # Tính toán vị trí theo xe tank
        rad_angle = math.radians(-self.tank.tank_angle)
        rotated_offset_x = offset_x * math.cos(rad_angle) - offset_y * math.sin(rad_angle)
        rotated_offset_y = offset_x * math.sin(rad_angle) + offset_y * math.cos(rad_angle)

        bar_x = self.tank.tank_rect.centerx + rotated_offset_x
        bar_y = self.tank.tank_rect.centery + rotated_offset_y

        # Lấy vị trí mới của hình ảnh sau khi xoay
        rotated_rect = rotated_health_bar.get_rect(center=(bar_x, bar_y))

        # Vẽ tại vị trí mới
        window.blit(rotated_health_bar, rotated_rect.topleft)