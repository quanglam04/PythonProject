import random

import pygame
from pygame import mixer
from tank import Tank
from tank_control import TankControl
import math
from bullet import Bullet
from StartScreen import result

class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True

        self.tank = Tank("asset/Blue Tank.png", window_width, window_height)
        self.control = TankControl(self.tank, window_width, window_height)
        self.bullets = []

        random_index = random.randint(1, 7)
        #random_index = 7
        self.map_data = read_map(f'MAP/map{random_index}.txt')

    def run(self, window):
        self.window = window

        # Cai dat am thanh
        mixer.init()
        mixer.music.load("asset/media.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        # Tạo viên đạn dựa trên vị trí và góc quay hiện tại của xe tăng
                        bullet = Bullet(self.tank.tank_rect.centerx + 20 * math.cos(math.radians(self.tank.tank_angle)),
                                        self.tank.tank_rect.centery - 20 * math.sin(math.radians(self.tank.tank_angle)),
                                        self.tank.tank_angle)
                        self.bullets.append(bullet)

            # Điều khiển xe tăng
            self.control.handle_input()

            # Cập nhật vị trí của xe tăng
            self.tank.tank_rect.x = int(self.tank.tank_x)
            self.tank.tank_rect.y = int(self.tank.tank_y)

            rotated_tank = pygame.transform.rotate(self.tank.tank_image, self.tank.tank_angle)
            new_rect = rotated_tank.get_rect(center=self.tank.tank_rect.center)

            # Vẽ bản đồ thay vì hình nền
            self.window.fill((255, 255, 255))  # Xóa màn hình với màu trắng
            draw_map(self.window, self.map_data, TILE_SIZE)

            # Vẽ xe tăng
            self.window.blit(rotated_tank, new_rect)
            for bullet in self.bullets[:]:
                bullet.move()
                if bullet.rect.bottom < 0:
                    self.bullets.remove(bullet)
                else:
                    bullet.draw(self.window)
            pygame.display.flip()

        pygame.quit()

# Cấu hình các hằng số
TILE_SIZE = 16

def read_map(file_path):
    with open(file_path, 'r') as file:
        map_data = [line.strip() for line in file]
    return map_data

def draw_map(window, map_data, tile_size):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':  # Tường
                color = (0, 0, 0)  # Màu đen
            elif tile == '0':  # Ô trống
                color = (255, 255, 255)  # Màu trắng
            elif tile == '*':  # Xe tăng của người chơi
                color = (0, 0, 255)  # Màu xanh
            elif tile == '-':  # Đối thủ
                color = (255, 0, 0)  # Màu đỏ
            else:
                continue
            pygame.draw.rect(window, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))