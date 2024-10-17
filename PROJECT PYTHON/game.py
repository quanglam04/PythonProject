import pygame
import Setting
from pygame import mixer
import button
from tank import load_map
from tank import Tank
from tank_control import TankControl
from tank_logic import TankLogic
from bullet import Bullet
import StartScreen
from tank import draw_health_bar
from explosion import Explosion
TILE_SIZE = 16
item = []

class TankGame:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True
        self.explosions_bull = []
        self.bullets = [[] for _ in range(StartScreen.result['numberOfPlayer'])]
        random_index = StartScreen.result['selected_map']
        self.map_data = read_map(f'MAP/map{random_index}.txt')
        self.spawn_points = load_map(random_index)
        self.tanks=[]
        self.initialize_tanks()

        self.map_mask,self.map_surface,self.item_name = create_map_mask(self.map_data,TILE_SIZE)

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
                tank.control = TankControl(tank, self.window_width, self.window_height, self.bullets[i], control_setting)
                self.tanks.append(tank)



    def run(self, window):
        start_time=0
        start_time_gun=0
        self.window = window

        # Cài đặt âm thanh
        setVolumn(0.0)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # # Vẽ bản đồ thay vì hình nền
            self.window.fill(Setting.YELLOW)  # Xóa màn hình với màu trắng
            draw_map(self.window, self.map_data, TILE_SIZE)

            for i, tank in enumerate(self.tanks):
                # Điều khiển xe tăng
                tank.check=False
                tank.control.handle_input()
                tank.update_tank_mask()
                if not tank.check :
                    tank.dx,tank.dy=0,0
                item_have=TankLogic.check_collision_with_items(tank,item,self.item_name,self.map_data,TILE_SIZE)
                if item_have == 3:
                    tank.speed_add += Setting.speedAdd
                    start_time=pygame.time.get_ticks()
                elif item_have ==1:
                    tank.health +=25
                elif item_have ==0:
                    tank.dame =50
                    start_time_gun=pygame.time.get_ticks()
                if tank.speed_add !=0 :
                    if pygame.time.get_ticks()-start_time >=10000:
                        tank.speed_add =0
                if tank.dame !=10 :
                    if pygame.time.get_ticks()-start_time_gun >=10000:
                        tank.dame=10
                if TankLogic.check_collision_with_wall(tank,self.map_mask):
                    tank.tank_x = tank.tank_x-tank.dx
                    tank.tank_y = tank.tank_y-tank.dy
                    tank.tank_angle = (tank.tank_angle-tank.d_angle) % 360
                    tank.update_tank_mask()
                    # print(tank.dx, tank.dy, tank.d_angle)
                for tank2 in self.tanks:
                    if tank2 is not tank:
                        if  TankLogic.check_collision_with_tank(tank, tank2):
                            tank.tank_x = tank.tank_x - tank.dx
                            tank.tank_y = tank.tank_y - tank.dy
                            tank.tank_angle = (tank.tank_angle - tank.d_angle) % 360
                            tank.update_tank_mask()
                            tank2.tank_x = tank2.tank_x - tank2.dx
                            tank2.tank_y = tank2.tank_y - tank2.dy
                            tank2.tank_angle = (tank2.tank_angle - tank2.d_angle) % 360
                            tank2.update_tank_mask()
                            break


                tank.tank_rect.x = int(tank.tank_x)
                tank.tank_rect.y = int(tank.tank_y)







                self.window.blit(tank.rotated_tank_image,tank.new_rect)
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
                            tank.health-=bullet.tank.dame
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

# def show_game_over_screen(window, window_width, window_height):
#     setVolumn(0)
#     # Hiển thị màn hình Game Over
#     font = pygame.font.Font(None, 150)
#     text = font.render("Game Over", True, (255, 0, 0))  # Chữ màu đỏ
#     window.fill((0, 0, 0))  # Làm màn hình đen
#     window.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))
#
#     # Hiển thị thông báo "Press Q to exit"
#     small_font = pygame.font.Font(None, 50)
#     sub_text = small_font.render("Press Q to exit", True, (255, 255, 255))  # Chữ màu trắng
#     window.blit(sub_text, (window_width // 2 - sub_text.get_width() // 2, window_height // 2 + text.get_height() // 2 + 20-10))
#
#
#     pygame.display.flip()  # Cập nhật màn hình
#
#     waiting_for_exit = True
#     while waiting_for_exit:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 waiting_for_exit = False  # Cho phép thoát bằng cách nhấn nút đóng cửa sổ
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:  # Nếu người chơi bấm phím Q
#                     waiting_for_exit = False
#
#
#     pygame.quit()  # Thoát pygame
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


def create_map_mask(map_data, tile_size=16):
    map_width = 1024
    map_height = 688
    wall = pygame.image.load(Setting.wall).convert()
    wall = pygame.transform.scale(wall, (tile_size , tile_size ))

    gunItem = pygame.image.load(Setting.gun).convert()
    gunItem.set_colorkey(Setting.WHITE)
    gunItem = pygame.transform.scale(gunItem, (tile_size+15, tile_size+15))
    gunItem_mask=pygame.mask.from_surface(gunItem)

    hpImage = pygame.image.load(Setting.hp).convert()
    hpImage.set_colorkey(Setting.WHITE)
    hpImage = pygame.transform.scale(hpImage, (tile_size+15, tile_size+15))
    hpImage_mask=pygame.mask.from_surface(hpImage)

    laser_gunItem = pygame.image.load(Setting.laser_gun).convert()
    laser_gunItem.set_colorkey(Setting.WHITE)
    laser_gunItem = pygame.transform.scale(laser_gunItem, (tile_size + 17, tile_size + 17))
    laser_gunItem_mask=pygame.mask.from_surface(laser_gunItem)

    speedItem = pygame.image.load(Setting.speed).convert()
    speedItem.set_colorkey(Setting.WHITE)
    speedItem = pygame.transform.scale(speedItem, (tile_size + 15, tile_size + 15))
    speedItem_mask= pygame.mask.from_surface(speedItem)

    x3Item = pygame.image.load(Setting.x3).convert()
    x3Item.set_colorkey(Setting.WHITE)
    x3Item = pygame.transform.scale(x3Item, (tile_size + 15, tile_size + 15))
    x3Item_mask = pygame.mask.from_surface(x3Item)
    map_surface = pygame.Surface((map_width, map_height),pygame.SRCALPHA)
    map_surface.fill((0, 0, 0,0))
    item_name=[gunItem_mask,hpImage_mask,laser_gunItem_mask,speedItem_mask,x3Item_mask]
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':  # Walls
                map_surface.blit(wall, (x * tile_size, y * tile_size))
            elif tile == '2':  # Item tăng sức mạnh (vũ khí)
                item.append((0,x,y))
            elif tile == '3':  # Item tăng máu (HP)
                item.append((1,x,y))
            elif tile == '4':  # Item tăng máu (HP)
                item.append((2,x,y))
            elif tile == '5':  # Item tăng máu (HP)
                item.append((3,x,y))
            elif tile == '6':  # Item tăng máu (HP)
                item.append((4,x,y))
    map_mask = pygame.mask.from_surface(map_surface)
    return map_mask, map_surface,item_name


