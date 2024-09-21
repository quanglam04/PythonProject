import random

import pygame
import Setting
from pygame import mixer

import button
from LoadingBar import screen
from StartScreen import result
from tank import Tank
from tank_control import TankControl
import tank_control
import math
from bullet import Bullet

item = []


# Cấu hình các hằng số
TILE_SIZE = 16


class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True



        self.bullets = []
        self.last_shot_time = 0
        self.bullet_time = 500  # 1000 mili giay == 1s
        self.bullet_sound = mixer.Sound(Setting.bulletMusic)
        self.bullet_sound.set_volume(0.4)
        random_index = result['selected_map']
        self.map_data = read_map(f'MAP/map{random_index}.txt')

        self.tank = Tank(Setting.TankBlue, window_width, window_height,random_index)
        self.control = TankControl(self.tank, window_width, window_height)

        # Lưu vị trí cuối cùng không va chạm
        self.last_valid_x = self.tank.tank_x
        self.last_valid_y = self.tank.tank_y
        self.last_valid_angle = self.tank.tank_angle  # Góc quay xe tăng

    def check_collision_with_walls(self, x, y):
        # Kiểm tra va chạm của xe tăng với các bức tường
        tank_rect = self.tank.tank_rect.copy()
        tank_rect.x = x
        tank_rect.y = y

        # Kiểm tra với từng ô trong bản đồ
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                if tile == '1':
                    wall_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if tank_rect.colliderect(wall_rect):
                        return True  # Va chạm với tường
        return False  # Không có va chạm

    def check_collision_with_items(self, x, y):
        # Kiểm tra va chạm của xe tăng với các item
        tank_rect = self.tank.tank_rect.copy()
        tank_rect.x = x
        tank_rect.y = y

        # Kiểm tra với từng ô trong bản đồ
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                if tile != '1' and tile !='0' and tile != '-' and tile!='*':  # Các item
                    item_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if tank_rect.colliderect(item_rect):
                        # Xóa item khỏi map sau khi va chạm
                        self.map_data[row_idx][col_idx] = '0'
                        return tile
        return None

    def check_bullet_collision(self):
        # Kiểm tra va chạm giữa đạn và xe tăng
        for bullet in self.bullets[:]:
            if self.tank.tank_rect.colliderect(bullet.rect):  # Kiểm tra va chạm
                # self.tank.health -= 20   Giảm máu xe tăng khi bị bắn trúng
                self.bullets.remove(bullet)  # Xóa đạn khỏi màn hình
                # Show hiệu ứng

            # Nếu xe tăng hết máu, kết thúc trò chơi
            # if self.tank.health <= 0:
            #     Show hiệu ứng nổ
            #     self.running = False

    def run(self, window):
        self.window = window

        # Cài đặt âm thanh
        setVolumn(0.5)

        while self.running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        # Tạo viên đạn dựa trên vị trí và góc quay hiện tại của xe tăng
                        if len(self.bullets) < 4 and current_time - self.last_shot_time >= self.bullet_time:
                            bullet = Bullet(
                                self.tank.tank_rect.centerx + 40 * math.cos(math.radians(self.tank.tank_angle)),
                                self.tank.tank_rect.centery - 40 * math.sin(math.radians(self.tank.tank_angle)),
                                self.tank.tank_angle)
                            self.bullets.append(bullet)
                            self.last_shot_time = current_time
                            self.bullet_sound.play()

            # Điều khiển xe tăng
            self.control.handle_input()

            # Cập nhật vị trí mới tạm thời cho xe tăng
            new_x = int(self.tank.tank_x)
            new_y = int(self.tank.tank_y)
            new_angle = self.tank.tank_angle

            # Kiểm tra va chạm với tường
            if self.check_collision_with_walls(new_x, new_y):
                self.tank.tank_x = self.last_valid_x
                self.tank.tank_y = self.last_valid_y
                self.tank.tank_angle = self.last_valid_angle
            else:
                self.last_valid_x = new_x
                self.last_valid_y = new_y
                self.last_valid_angle = new_angle
                self.tank.tank_rect.x = new_x
                self.tank.tank_rect.y = new_y

            # Kiểm tra va chạm với item
            item_collision = self.check_collision_with_items(new_x, new_y)
            if item_collision != None:
                if item_collision == str(5):
                    Setting.speedAdd = 1
                item.append(item_collision)

            rotated_tank = pygame.transform.rotate(self.tank.tank_image, self.tank.tank_angle)
            new_rect = rotated_tank.get_rect(center=self.tank.tank_rect.center)

            # Vẽ bản đồ thay vì hình nền
            self.window.fill(Setting.WHITE)  # Xóa màn hình với màu trắng
            draw_map(self.window, self.map_data, TILE_SIZE)

            # Vẽ xe tăng
            self.window.blit(rotated_tank, new_rect)

            # Vẽ đạn
            self.check = False
            for bullet in self.bullets[:]:
                bullet.move(self.map_data, TILE_SIZE)
                if bullet.is_expired_bullet():
                    self.bullets.remove(bullet)
                else:
                    bullet.draw(self.window)

                if check_collision(self.tank, bullet):
                    self.check = True
                    show_game_over_screen(self.window, self.window_width, self.window_height)
                    break

            if self.check == False:
                pygame.display.flip()
            else:
                self.running = False
        pygame.quit()

def check_collision(tank, bullet):
    return tank.tank_rect.colliderect(bullet.rect)

def read_map(file_path):
    with open(file_path, 'r') as file:
        map_data = [list(line.strip()) for line in file]
    return map_data
def show_game_over_screen(window, window_width, window_height):
    setVolumn(0)
    # Hiển thị màn hình Game Over
    font = pygame.font.Font(None, 150)
    text = font.render("Game Over", True, (255, 0, 0))  # Chữ màu đỏ
    window.fill((0, 0, 0))  # Làm màn hình đen
    window.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))

    # Hiển thị thông báo "Press Q to exit"
    small_font = pygame.font.Font(None, 50)
    sub_text = small_font.render("Press Q to exit", True, (255, 255, 255))  # Chữ màu trắng
    window.blit(sub_text, (window_width // 2 - sub_text.get_width() // 2, window_height // 2 + text.get_height() // 2 + 20-10))


    pygame.display.flip()  # Cập nhật màn hình

    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_exit = False  # Cho phép thoát bằng cách nhấn nút đóng cửa sổ
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Nếu người chơi bấm phím Q
                    waiting_for_exit = False


    pygame.quit()  # Thoát pygame
def setVolumn(x):
    mixer.init()
    mixer.music.load(Setting.backgroundMusic)
    mixer.music.set_volume(x)
    mixer.music.play()

def draw_map(window, map_data, tile_size):
    wall = pygame.image.load(Setting.wall).convert()
    wall = pygame.transform.scale(wall, (tile_size , tile_size ))

    gunItem = pygame.image.load(Setting.gun).convert()
    gunItem.set_colorkey(Setting.WHITE)
    gunItem = pygame.transform.scale(gunItem, (tile_size+15, tile_size+15))

    hpImage = pygame.image.load(Setting.hp).convert()
    hpImage.set_colorkey(Setting.WHITE)
    hpImage = pygame.transform.scale(hpImage, (tile_size+15, tile_size+15))

    laser_gunItem = pygame.image.load(Setting.laser_gun).convert()
    laser_gunItem.set_colorkey(Setting.WHITE)
    laser_gunItem = pygame.transform.scale(laser_gunItem, (tile_size + 17, tile_size + 17))

    speedItem = pygame.image.load(Setting.speed).convert()
    speedItem.set_colorkey(Setting.WHITE)
    speedItem = pygame.transform.scale(speedItem, (tile_size + 15, tile_size + 15))

    x3Item = pygame.image.load(Setting.x3).convert()
    x3Item.set_colorkey(Setting.WHITE)
    x3Item = pygame.transform.scale(x3Item, (tile_size + 15, tile_size + 15))
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':  # Tường
                window.blit(wall, (x * tile_size, y * tile_size))  # Vẽ ảnh súng
            elif tile == '-':  # Đối thủ
                color = (255, 0, 0)  # Màu đỏ
                pygame.draw.rect(window, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            elif tile == '2':  # Item tăng sức mạnh (vũ khí)
                window.blit(gunItem, (x * tile_size, y * tile_size))  # Vẽ ảnh súng
            elif tile == '3':  # Item tăng máu (HP)
                window.blit(hpImage, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '4':  # Item tăng máu (HP)
                window.blit(laser_gunItem, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '5':  # Item tăng máu (HP)
                window.blit(speedItem, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '6':  # Item tăng máu (HP)
                window.blit(x3Item, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu

