import pygame
import Setting
from Sound import ls_item_s,mg_item_s,missile_active_sound,tank_death_sound,missile_crash_tank_sound,normal_sound_crash
import Static_object
from tank import load_map
from tank import Tank
from tank_control import TankControl
from tank_logic import TankLogic
import StartScreen
from tank import draw_health_bar
import Static_object as St
from explosion import Explosion
from shield import Shield
TILE_SIZE = Setting.tile_size
item = []
from Laser_Aiming_Line import LaserAiming
class TankGame:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True
        self.explosions_bull = []
        self.missiles=[]
        self.bullets = []
        self.lasers=[]
        random_index = StartScreen.result['selected_map']
        self.map_data = read_map(f'MAP/map{random_index}.txt')
        self.map_optimize= load_wall_rect(f'MAP/Optimize_structure_in_map/map{random_index}optimize.txt')
        self.collision_map=[]

        self.informationOfTank = pygame.image.load(Setting.informationOfTank)

        if Setting.informationOfTank == 'asset/Stats/one-player.png':
            self.informationOfTank = pygame.transform.scale(self.informationOfTank, (300, 500))
        elif Setting.informationOfTank == 'asset/Stats/two-player.png':
            self.informationOfTank = pygame.transform.scale(self.informationOfTank, (450, 500))
        elif Setting.informationOfTank == 'asset/Stats/three-player.png':
            self.informationOfTank = pygame.transform.scale(self.informationOfTank, (600, 500))
        else:
            self.informationOfTank = pygame.transform.scale(self.informationOfTank, (750, 500))

        self.show_info = False

        self.spawn_points = load_map(random_index)
        self.tanks=[]
        self.initialize_tanks()

        self.map_mask,self.map_surface,self.item_name = create_map_mask(self.map_data,TILE_SIZE)

        for rect in self.map_optimize:
            x,y,width,height=rect
            self.collision_map.append(pygame.Rect(x*TILE_SIZE,y*TILE_SIZE,width*TILE_SIZE,height*TILE_SIZE))
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

                if i == 0:
                    # tank_path = Setting.TankBlue
                    # image_name = Setting.Blue_image
                    # color=Setting.BLUE
                    control_setting = control_settings_player_1
                elif i == 1:
                    # tank_path = Setting.TankRed
                    # image_name=Setting.Red_image
                    # color=Setting.RED
                    control_setting = control_settings_player_2
                elif i == 2:
                    # tank_path = Setting.TankOrange
                    # image_name=Setting.Orange_image
                    # color=Setting.ORANGE
                    control_setting = control_settings_player_3
                else:
                    # tank_path = Setting.TankGreen
                    # image_name=Setting.Green_image
                    # color=Setting.GREEN
                    control_setting = control_settings_player_4
                if i < len(self.spawn_points):
                    pos = self.spawn_points[i]
                else:
                    pos = (0, 0)
                tank = Tank(pos,i)
                tank.control = TankControl(tank, self.window_width, self.window_height, self.bullets,self.lasers,self.missiles ,control_setting)
                self.tanks.append(tank)



    def run(self, window):



        start_time=0
        start_time_gun=0
        self.window = window
        start_time = pygame.time.get_ticks()
        while self.running:

            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Đổi từ mili giây sang giây
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            time_text = f"Time: {minutes:02}:{seconds:02}"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.show_info = True  # Hiển thị ảnh khi nhấn Tab
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_TAB:
                        self.show_info = False  # Ẩn ảnh khi thả phím Tab



            # window.fill((0, 0, 0))
            # # Vẽ bản đồ thay vì hình nền

            self.window.fill(Setting.YELLOW)  # Xóa màn hình với màu trắng
            draw_map(self.window, self.map_data, TILE_SIZE)


            for tank in self.tanks:
                # Điều khiển xe tăng
                tank.check=False
                tank.control.handle_input(self.explosions_bull)
                tank.update_tank_mask()
                if not tank.check :
                    tank.dx,tank.dy=0,0
                item_have=TankLogic.check_collision_with_items(tank,item,self.item_name,self.map_data,TILE_SIZE)
                if item_have == 3:
                    tank.speed_add += Setting.speedAdd
                    start_time=pygame.time.get_ticks()
                elif item_have ==1:
                    tank.health +=25
                elif item_have == 0:
                    tank.dame_bonus =10
                    start_time_gun=pygame.time.get_ticks()
                    tank.bullet_color=Setting.tanks_color[tank.id]
                elif item_have == 4:
                    tank.shield_active=True
                    tank.shield_health=4
                    tank.shield=Shield(tank)
                elif item_have == 5:
                    tank.gun_mode = 2
                    tank.update_tank_image(St.laser_tanks[tank.id])
                    ls_item_s.play()

                elif item_have == 6:
                    tank.gun_mode= 3
                    tank.minigun_bull_count=0
                    tank.update_tank_image(St.machine_tanks[tank.id])
                    mg_item_s.play()
                elif item_have ==7:
                    tank.gun_mode =4
                    tank.update_tank_image(St.missile_tanks[tank.id])
                    missile_active_sound.play()
                if tank.speed_add !=0 :
                    if pygame.time.get_ticks()-start_time >=10000:
                        tank.speed_add =0
                if tank.dame_bonus :
                    if pygame.time.get_ticks()-start_time_gun >=10000:
                        tank.dame_bonus=0
                        tank.update_tank_image(St.normal_tanks[tank.id])
                        tank.bullet_color=Setting.BLACK
                if tank.gun_mode ==3 and tank.minigun_bull_count ==18:
                    tank.gun_mode=1
                    tank.update_tank_image(St.normal_tanks[tank.id])

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


                if tank.gun_mode==2:
                    tank.tank_laser = LaserAiming(tank.tank_x , tank.tank_y , tank.tank_angle, self.window_width,
                                                  self.window_height, self.map_data)
                    tank.tank_laser.active=True
                    tank.tank_laser.update(tank.tank_rect.centerx,tank.tank_rect.centery,tank.tank_angle)
                    tank.laser_endpoints=[]
                    while tank.tank_laser.remaining_length >0:
                        tank.tank_laser.calculate_end_point(self.collision_map)
                        tank.laser_endpoints.append((tank.tank_laser.end_x,tank.tank_laser.end_y))
                        tank.tank_laser.draw_2_line(self.window,Setting.tanks_color[tank.id])

                        tank.tank_laser.x=tank.tank_laser.end_x
                        tank.tank_laser.y=tank.tank_laser.end_y

                        if tank.tank_laser.normal[0] !=0:
                            tank.tank_laser.angle=180-tank.tank_laser.angle
                        else:
                            tank.tank_laser.angle = 360 - tank.tank_laser.angle
                self.window.blit(tank.rotated_tank_image,tank.new_rect)
                draw_health_bar(tank,window)
                if tank.shield_active:
                    tank.shield.update_pos()
                    tank.shield.draw(self.window)

            for bullet in self.bullets:
                bullet.move(self.map_data,TILE_SIZE)
                if bullet.is_expired_bullet():
                    if bullet.radius >=5:
                        explosion = Explosion(bullet.rect.centerx, bullet.rect.centery,Static_object.expl_1_frames,1000)
                        self.explosions_bull.append(explosion)
                    self.bullets.remove(bullet)
                else:
                    bullet.draw(self.window)
                for tank in self.tanks:
                    if TankLogic.check_collision(tank,bullet):
                        explosion = Explosion(bullet.rect.centerx, bullet.rect.centery,Static_object.expl_1_frames,1000)
                        self.explosions_bull.append(explosion)
                        if tank.shield_active :
                            tank.shield_health -=1
                            if tank.shield_health ==0:
                                tank.shield_active= False
                        else:
                            tank.health = tank.health- bullet.dame()-bullet.tank.dame_bonus
                        normal_sound_crash.play()
                        self.bullets.remove(bullet)

                        break
            for laser in self.lasers:
                if laser.tank.tank_laser.active: #trong  vai ms thi cau lenh an nut shot co the da tao ra nhieu laser, ta chi lay duy nhat mot cai
                    laser.laser_move()
                    if laser.is_expired_bullet():
                        laser.draw(self.window)
                        self.lasers.remove(laser)
                        laser.tank.tank_laser.active = False #khi como
                    else:
                        for tank in self.tanks:
                                x,y=TankLogic.check_collision_with_laser(tank,laser)
                                if x is not None and y is not None :
                                    laser.end_x,laser.end_y=x,y
                                    laser.draw(self.window)
                                    self.lasers.remove(laser)
                                    laser.tank.tank_laser.active= False #khi co mot tia va cham roi thi cac tia o ngay sau se khong dc tinh nua
                                    if tank.shield_active:
                                        tank.shield_health -= 1
                                        if tank.shield_health == 0:
                                            tank.shield_active = False
                                    else:
                                        tank.health = tank.health- laser.dame -laser.tank.dame_bonus
                                    explosion=Explosion(x,y,Static_object.expl_1_frames,1000)

                                    self.explosions_bull.append(explosion)
                                    break
                        laser.draw(self.window)
            for missile in self.missiles:
                if missile.missile_bug_handle(self.map_data):
                    explosion=Explosion(missile.x,missile.y,St.expl_1_frames,1000)
                    self.explosions_bull.append(explosion)
                    self.missiles.remove(missile)
                    continue
                missile.check_collision_with_wall(self.map_data)
                missile.update_tank_pos(self.tanks)
                missile.missile_path(self.map_data)
                missile.draw(self.window)
                explosion=missile.create_smoke_fame()
                if explosion is not None:
                    self.explosions_bull.append(explosion)
                for tank in self.tanks:
                    if TankLogic.check_collision_with_missile(tank,missile):
                        if tank.shield_active :
                            tank.shield_health -=1
                            if tank.shield_health ==0:
                                tank.shield_active= False
                        else:
                            tank.health = tank.health- missile.dame-missile.tank.dame_bonus
                        explosion=Explosion(missile.img_rect.centerx,missile.img_rect.centery,St.expl_1_frames,1000)
                        self.explosions_bull.append(explosion)
                        self.missiles.remove(missile)
                        missile_crash_tank_sound.play()


            for tank in self.tanks:
                if tank.health <= 0:
                    explosion=Explosion(tank.tank_rect.centerx, tank.tank_rect.centery,Static_object.expl_4_frames,1000)
                    self.explosions_bull.append(explosion)
                    self.tanks.remove(tank)
                    tank_death_sound.play()
            for explosion in self.explosions_bull[:]:
                explosion.update()

                explosion.draw(self.window)

                if explosion.image is None:
                    self.explosions_bull.remove(explosion)

            font = pygame.font.Font(None, 36)  # Khởi tạo font chữ, kích thước 36
            time_surface = font.render(time_text, True, (0, 0, 0))  # Vẽ thời gian với màu đen
            time_rect = time_surface.get_rect(midbottom=(self.window.get_width() // 2, self.window.get_height() - 10))
            self.window.blit(time_surface, time_rect)

            if self.show_info:
                image_rect = self.informationOfTank.get_rect(center=self.window.get_rect().center)
                self.window.blit(self.informationOfTank, image_rect)
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


def read_map(file_path):
    with open(file_path, 'r') as file:
        map_data = [list(line.strip()) for line in file]
    return map_data

def draw_map(window, map_data, tile_size):

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':  # Tường
                window.blit(St.wall, (x * tile_size, y * tile_size))  # Vẽ ảnh súng
            elif tile == '2':  # Item tăng sức mạnh (vũ khí)
                window.blit(St.gunItem, (x * tile_size, y * tile_size))  # Vẽ ảnh súng
            elif tile == '3':  # Item tăng máu (HP)
                window.blit(St.hpImage, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '4':  # Item tăng máu (HP)
                window.blit(St.laser_gunItem, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '5':  # Item tăng máu (HP)
                window.blit(St.speedItem, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '6':  # Item tăng máu (HP)
                window.blit(St.shield_item, (x * tile_size, y * tile_size))  # Vẽ ảnh tăng máu
            elif tile == '7':
                window.blit(St.laser_line,(x*tile_size,y*tile_size))
            elif tile =='8':
                window.blit(St.machine_gun,(x*tile_size,y*tile_size)) # day la check sung may ma
            elif tile=='9':
                window.blit(St.missile_item,(x*tile_size,y*tile_size))

def create_map_mask(map_data, tile_size=16):
    map_width = 1024
    map_height = 688
    # wall = pygame.image.load(Setting.wall).convert()
    # wall = pygame.transform.scale(wall, (tile_size , tile_size ))

    gunItem_mask=pygame.mask.from_surface(St.gunItem)

    hpImage_mask=pygame.mask.from_surface(St.hpImage)


    laser_gunItem_mask=pygame.mask.from_surface(St.laser_gunItem)


    speedItem_mask= pygame.mask.from_surface(St.speedItem)


    shield_item_mask = pygame.mask.from_surface(St.shield_item)


    laser_line_mask = pygame.mask.from_surface(St.laser_line)

    machine_gun_mask=pygame.mask.from_surface(St.machine_gun)

    missile_item_mask=pygame.mask.from_surface(St.missile_item)

    map_surface = pygame.Surface((map_width, map_height),pygame.SRCALPHA)
    map_surface.fill((0, 0, 0,0))
    item_name=[gunItem_mask,hpImage_mask,laser_gunItem_mask,speedItem_mask,shield_item_mask,laser_line_mask,machine_gun_mask,missile_item_mask]
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':  # Walls
                map_surface.blit(St.wall, (x * tile_size, y * tile_size))
            elif tile == '2':  # Item tăng sức mạnh (vũ khí)
                item.append((0,x*tile_size,y*tile_size))
            elif tile == '3':  # Item tăng máu (HP)
                item.append((1,x*tile_size,y*tile_size))
            elif tile == '4':  # Item tăng máu (HP)
                item.append((2,x*tile_size,y*tile_size))
            elif tile == '5':  # Item tăng máu (HP)
                item.append((3,x*tile_size,y*tile_size))
            elif tile == '6':  # Item tăng máu (HP)
                item.append((4,x*tile_size,y*tile_size))
            elif tile== '7':
                item.append((5,x*tile_size,y*tile_size))
            elif tile =='8':
                item.append((6,x*tile_size,y*tile_size))
            elif tile == '9':
                item.append((7,x*tile_size,y*tile_size))
    map_mask = pygame.mask.from_surface(map_surface)
    return map_mask, map_surface,item_name


def load_wall_rect(filename):
    rect_walls = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    rect = tuple(map(int, line.split()))
                    if len(rect) == 4:
                        rect_walls.append(rect)
                    else:
                        print(f"Invalid rectangle, wrong number of values: {line}")
                except ValueError as e:
                    print(f"Error parsing line '{line}': {e}")
    return rect_walls
