import pygame
import Setting
from pygame import mixer

import button
from StartScreen import result
from tank import load_map
from tank import Tank
from tank_control import TankControl
from tank_logic import TankLogic
from bullet import Bullet
import StartScreen
item = []
from tank import draw_health_bar

from explosion import Explosion
TILE_SIZE = 16


class TankGame:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True
        self.explosions_bull = []
        self.bullets = [[] for _ in range(StartScreen.result['numberOfPlayer'])]
        random_index = result['selected_map']
        self.map_data = read_map(f'MAP/map{random_index}.txt')
        self.spawn_points = load_map(random_index)
        self.tanks=[]
        self.controls=[]
        self.last_valid_x=[]
        self.last_valid_y=[]
        self.last_valid_angle=[]
        self.initialize_tanks()

    def initialize_tanks(self):
        control_settings_player_1 = {
            'up': Setting.up_player_1,
            'down': Setting.down_player_1,
            'left': Setting.left_player_1,
            'right': Setting.right_player_1,
            'shoot': Setting.hit_player_1
        }

        control_settings_player_2 = {
            'up': Setting.up_player_2,
            'down': Setting.down_player_2,
            'left': Setting.left_player_2,
            'right': Setting.right_player_2,
            'shoot': Setting.hit_player_2
        }
        control_settings_player_3 = {
            'up': Setting.up_player_3,
            'down': Setting.down_player_3,
            'left': Setting.left_player_3,
            'right': Setting.right_player_3,
            'shoot': Setting.hit_player_3
        }

        control_settings_player_4 = {
            'up': Setting.up_player_4,
            'down': Setting.down_player_4,
            'left': Setting.left_player_4,
            'right': Setting.right_player_4,
            'shoot': Setting.hit_player_4
        }

        for i in range(StartScreen.result['numberOfPlayer']):
                tank_path = None
                control_setting = None
                pos = None

                if i == 0:
                    tank_path = Setting.Tank_blue
                    control_setting = control_settings_player_1
                elif i == 1:
                    tank_path = Setting.Tank_red
                    control_setting = control_settings_player_2
                elif i == 2:
                    tank_path = Setting.Tank_sand
                    control_setting = control_settings_player_3
                else:
                    tank_path = Setting.Tank_green
                    control_setting = control_settings_player_4


                if i < len(self.spawn_points):
                    pos = self.spawn_points[i]
                else:
                    pos = (0, 0)


                tank = Tank(tank_path, pos)
                control = TankControl(tank, self.window_width, self.window_height, self.bullets[i], control_setting)
                self.tanks.append(tank)
                self.controls.append(control)


                self.last_valid_x.append(tank.tank_x)
                self.last_valid_y.append(tank.tank_y)
                self.last_valid_angle.append(tank.tank_angle)


    def run(self, window):
        self.window = window
        # Cài đặt âm thanh
        setVolumn(0.5)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Điều khiển xe tăng
            for control in self.controls:
                control.handle_input()
            # # Vẽ bản đồ thay vì hình nền
            self.window.fill(Setting.WHITE)  # Xóa màn hình với màu trắng
            draw_map(self.window, self.map_data, TILE_SIZE)

            for i, tank in enumerate(self.tanks):
                new_x = int(tank.tank_x)
                new_y = int(tank.tank_y)


                if TankLogic.check_collision_with_walls(tank, new_x, new_y, TILE_SIZE, self.map_data):
                    tank.tank_x = self.last_valid_x[i]
                    tank.tank_y = self.last_valid_y[i]
                    tank.tank_angle = self.last_valid_angle[i]
                else:
                    self.last_valid_x[i] = new_x
                    self.last_valid_y[i] = new_y
                    self.last_valid_angle[i] = tank.tank_angle
                    tank.tank_rect.x = new_x
                    tank.tank_rect.y = new_y


                item_collision = TankLogic.check_collision_with_items(tank, new_x, new_y, TILE_SIZE, self.map_data)
                if item_collision is not None:
                    if item_collision == str(5):
                        Setting.speedAdd = 1
                    item.append(item_collision)
                rotated_tank = pygame.transform.rotate(tank.tank_image, tank.tank_angle)
                new_rect = rotated_tank.get_rect(center=tank.tank_rect.center)
                self.window.blit(rotated_tank, new_rect)
                draw_health_bar(tank,window)






            for i in range(len(self.bullets)):
                bullets_to_remove = []

                for j in range(len(self.bullets[i])):
                    bullet = self.bullets[i][j]
                    bullet.move(self.map_data, 16)
                    if bullet.is_expired_bullet():
                        explosion = Explosion(bullet.rect.centerx, bullet.rect.centery, "asset/explosion 1.png", 256,
                                              256)
                        self.explosions_bull.append(explosion)
                        bullets_to_remove.append(j)
                    else:
                        bullet.draw(self.window)
                    for tank in self.tanks:
                        if TankLogic.check_collision(tank, bullet):
                            explosion = Explosion(bullet.rect.centerx, bullet.rect.centery, "asset/explosion 1.png",
                                                  256, 256)
                            self.explosions_bull.append(explosion)
                            tank.health-=25
                            if tank.health==0:
                                explosion=Explosion(tank.tank_rect.centerx,tank.tank_rect.centery,"asset/explosion 4.png",256,256)
                                self.explosions_bull.append(explosion)
                                self.tanks.remove(tank)
                            bullets_to_remove.append(j)
                            break
                for j in reversed(bullets_to_remove):
                    self.bullets[i].pop(j)
            for explosion in self.explosions_bull[:]:
                explosion.update()
                explosion.draw(self.window)
                if explosion.image is None:
                    self.explosions_bull.remove(explosion)

            pygame.display.flip()


        pygame.quit()

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


def read_map(file_path):
    with open(file_path, 'r') as file:
        map_data = [list(line.strip()) for line in file]
    return map_data

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
