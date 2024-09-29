import random
import pygame
from pygame import mixer
from tank import Tank
from tank_control import TankControl
import math
from bullet_Lazer import Laser
from Laser_Aiming_Line import LaserAiming

class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True

        self.tank = Tank("asset/Blue Tank.png", window_width, window_height)
        self.control = TankControl(self.tank, window_width, window_height)

        self.bullets = []
        self.last_shot_time=0
        self.bullet_time=500 #1000 mili giay == 1s
        self.bullet_sound=mixer.Sound("asset/normal bullet.flac")
        self.bullet_sound.set_volume(0.4)

        random_index = random.randint(1, 2)
        self.map_data = read_map(f'MAP/map{random_index}.txt')

        #Khoi tao laser aim line
        self.laser_aiming = LaserAiming(self.tank.tank_rect.centerx, self.tank.tank_rect.centery, self.tank.tank_angle, window_width, window_height, self.map_data)

    def run(self, window):
        self.window = window

        # Cai dat am thanh
        mixer.init()
        mixer.music.load("asset/media.mp3")
        mixer.music.set_volume(0.4)
        mixer.music.play()
        while self.running:
            current_time=pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        # Tạo viên đạn dựa trên vị trí và góc quay hiện tại của xe tăng
                        self.laser_aiming.turn_off_Laser()
                        if len(self.bullets) < 4 and current_time-self.last_shot_time >=self.bullet_time :
                            bullet = Laser(self.tank.tank_rect.centerx + 20 * math.cos(math.radians(self.tank.tank_angle)),
                                            self.tank.tank_rect.centery - 20 * math.sin(math.radians(self.tank.tank_angle)),
                                            self.tank.tank_angle)
                            self.bullets.append(bullet)
                            self.last_shot_time=current_time
                            self.bullet_sound.play()

            # Turn laser back on after shooting cooldown
            if current_time - self.last_shot_time >= self.bullet_time:
                self.laser_aiming.turn_on_Laser()

            # Điều khiển xe tăng
            self.control.handle_input()

            # Cập nhật vị trí của xe tăng
            self.tank.tank_rect.x = int(self.tank.tank_x)
            self.tank.tank_rect.y = int(self.tank.tank_y)
            self.laser_aiming.update(self.tank.tank_rect.centerx, self.tank.tank_rect.centery, self.tank.tank_angle)

            rotated_tank = pygame.transform.rotate(self.tank.tank_image, self.tank.tank_angle)
            new_rect = rotated_tank.get_rect(center=self.tank.tank_rect.center)

            # Vẽ bản đồ thay vì hình nền
            self.window.fill((255, 255, 255))  # Xóa màn hình với màu trắng
            draw_map(self.window, self.map_data, TILE_SIZE)

            # Vẽ tia laser: Phải vẽ trước xe tăng, để ảnh xe tăng đè lên.
            if self.laser_aiming.active:
                 self.laser_aiming.remaining_length = 500
                 while self.laser_aiming.remaining_length > 0:
                    self.laser_aiming.calculate_end_point()
                    self.laser_aiming.draw_2_line(window)

                    #Update the location of self.x, self.y
                    self.laser_aiming.x = self.laser_aiming.end_x
                    self.laser_aiming.y = self.laser_aiming.end_y
                    if self.laser_aiming.normal[0] != 0:
                        self.laser_aiming.angle = 180 - self.laser_aiming.angle
                    else:
                        self.laser_aiming.angle = 360 - self.laser_aiming.angle

            # Vẽ xe tăng
            self.window.blit(rotated_tank, new_rect)

            for bullet in self.bullets[:]:
                bullet.move(self.map_data, TILE_SIZE)
                if bullet.is_expired_bullet():
                    self.bullets.remove(bullet)
                else:
                    bullet.draw(self.window)
            pygame.display.flip()

        pygame.quit()


# Cấu hình các hằng số
TILE_SIZE = 16

def read_map(file_path):
    tmp_data = []
    with open(file_path, 'r') as file:
        for line in file:
            a = []
            for i in line.strip():
                if i == '0':
                    a.append(0)
                if i == '1':
                    a.append(1)
                if i == '*':
                    a.append(3)
                if i == '-':
                    a.append(4)

            tmp_data.append(a)
    return tmp_data


def draw_map(window, map_data, tile_size):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:  # Tường
                color = (0, 0, 0)  # Màu đen
            elif tile == 0:  # Ô trống
                color = (255, 255, 255)  # Màu trắng
            elif tile == 2:  # Xe tăng của người chơi
                color = (0, 0, 255)  # Màu xanh
            elif tile == 3:  # Đối thủ
                color = (255, 0, 0)  # Màu đỏ
            else:
                continue
            pygame.draw.rect(window, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
