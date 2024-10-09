import random
import pygame
import numpy as np
import math
from pygame import mixer
from tank import Tank
from tank_control import TankControl
from bullet_Lazer import Laser
from Laser_Aiming_Line import LaserAiming
from bullet_logic import Bullet_logic
from bullet_nomal import Bullet_normal


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

        self.collision_map = []

        map_test = np.copy(self.map_data)
        # 4 buc tuong xung quanh
        self.collision_map.append(pygame.Rect(0 * 16, 0 * 16, 16, 16 * 43))
        self.collision_map.append(pygame.Rect(1 * 16, 0 * 16, 16 * 63, 16 * 1))
        self.collision_map.append(pygame.Rect(63 * 16, 1 * 16, 16, 16 * 42))
        self.collision_map.append(pygame.Rect(1 * 16, 42 * 16, 16 * 62, 16))
        # Cac buc tuong trong map
        for i in range(1, 42):
            row = map_test[i]
            start = -1
            length = 0
            for j in range(1, 63):
                if row[j] == 1:
                    if length == 0:
                        start = j
                        length += 1
                    else:
                        length += 1
                        if j == 62 and length >= 2:
                            self.collision_map.append(pygame.Rect(start * 16, i * 16, length * 16, 16))
                            for x in range(start, start + length):
                                map_test[i][x] = 0
                elif length >= 2:  # row[j] = 0 and length >=2
                    self.collision_map.append(pygame.Rect(start * 16, i * 16, length * 16, 16))
                    for x in range(start, start + length):
                        map_test[i][x] = 0
                    length = 0
                else:
                    length = 0  # row[j] = 0 and length <2
        for j in range(1, 63):
            start = -1
            length = 0
            for i in range(1, 42):
                if map_test[i][j] == 1:
                    if length == 0:
                        start = i
                        length += 1
                    else:
                        length += 1
                        if i == 41:
                            self.collision_map.append(pygame.Rect(j * 16, start * 16, 16, length * 16))
                elif length:
                    self.collision_map.append(pygame.Rect(j * 16, start * 16, 16, length * 16))
                    length = 0


    def run(self, window):
        self.window = window

        # Cai dat am thanh
        mixer.init()
        mixer.music.load("asset/media.mp3")
        mixer.music.set_volume(0.0)
        mixer.music.play()

        bullet_Counter = 1 # (= 0 : Đạn lazer); (= 1 Đạn thường); (= 2 Đạn chùm)

        while self.running:
            current_time=pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                    if event.key == pygame.K_SPACE:

                        if bullet_Counter == 0 :
                            # Đạn lazer
                            if len(self.bullets) < 4 and current_time-self.last_shot_time >=self.bullet_time :
                                bullet = Laser(self.tank.tank_rect.centerx + 20 * math.cos(math.radians(self.tank.tank_angle)),
                                                self.tank.tank_rect.centery - 20 * math.sin(math.radians(self.tank.tank_angle)),
                                                self.tank.tank_angle)
                                self.bullets.append(bullet)
                                
                        
                        if bullet_Counter == 1 :
                            # Đạn thường
                            if len(self.bullets) < 4 and current_time-self.last_shot_time >=self.bullet_time :
                                bullet = Bullet_normal(self.tank.tank_rect.centerx + 35 * math.cos(math.radians(self.tank.tank_angle)),
                                                self.tank.tank_rect.centery - 35 * math.sin(math.radians(self.tank.tank_angle)),
                                                self.tank.tank_angle)
                                self.bullets.append(bullet)
                                

                        if bullet_Counter == 2 :
                            # Đạn chùm
                            if current_time - self.last_shot_time >= self.bullet_time :
                                
                                for i in range(10):
                                    spread_angle = self.tank.tank_angle + (i - 5) * 2  # Điều chỉnh góc phát tán

                                    bullet = Bullet_normal(
                                    self.tank.tank_rect.centerx + 35 * math.cos(math.radians(self.tank.tank_angle)),
                                    self.tank.tank_rect.centery - 35 * math.sin(math.radians(self.tank.tank_angle)),
                                    spread_angle)

                                    
                                    self.bullets.append(bullet)
                        self.last_shot_time = current_time
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
            # if self.laser_aiming.active:
            #      self.laser_aiming.remaining_length = 500       #Khởi tạo lại remaining_length = 500 (do tia laser cũ đã bị trừ hết rồi)
            #      while self.laser_aiming.remaining_length > 0:
            #         self.laser_aiming.calculate_end_point(self.collision_map)
            #         self.laser_aiming.draw_2_line(window)

            #         #Update the location of self.x, self.y
            #         self.laser_aiming.x = self.laser_aiming.end_x
            #         self.laser_aiming.y = self.laser_aiming.end_y
            #         if self.laser_aiming.normal[0] != 0:
            #             self.laser_aiming.angle = 180 - self.laser_aiming.angle
            #         else:
            #             self.laser_aiming.angle = 360 - self.laser_aiming.angle


            # Vẽ xe tăng
            self.window.blit(rotated_tank, new_rect)

            # Vẽ đạn
            for bullet in self.bullets[:]:
                if bullet.is_expired_bullet():
                    self.bullets.remove(bullet)
                else:
                    #Tinh end_x, end_y
                    bullet.cal_end_point(self.collision_map)

                    #Ve dan 
                    bullet.draw(window)

                    #Cap nhat lai x, y, angle của bullet để chuẩn bị cho hàm run tiếp theo
                    bullet.update()
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