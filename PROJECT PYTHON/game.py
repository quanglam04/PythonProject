import random
import pygame
from pygame import mixer
from player import Player
import math
from bullet import Bullet
from explosion import Explosion

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True

        self.players = [
            Player("asset/tank_blue.png", window_width, window_height, 100, 100,
                   {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d,
                    'shoot': pygame.K_SPACE}, 1),
            Player("asset/tank_red.png", window_width, window_height, window_width - 100, window_height - 100,
                   {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT,
                    'shoot': pygame.K_KP0}, 2),
            Player("asset/tank_sand.png", window_width, window_height, window_width - 100, 100,
                   {'up': pygame.K_KP8, 'down': pygame.K_KP2, 'left': pygame.K_KP4, 'right': pygame.K_KP6,
                    'shoot': pygame.K_KP1}, 3),
            Player("asset/tank_green.png", window_width, window_height, 50, window_height - 220,
                   {'up': pygame.K_i, 'down': pygame.K_k, 'left': pygame.K_j, 'right': pygame.K_l,
                    'shoot': pygame.K_h}, 4)
        ]

        self.bullets = []
        self.last_shot_time = [0, 0, 0, 0] #4 người chơi nên cho 4 ô, ban đầu có 2 nên bị lỗi out of index
        self.bullet_time = 500
        self.bullet_sound = mixer.Sound("asset/normal bullet.flac")
        self.bullet_sound.set_volume(0.4)
        self.explosions_bull = []
        random_index = random.randint(1, 2)
        self.map_data = read_map(f'MAP/map{random_index}.txt')
    #check va chạm với tường
    def check_collision_with_walls(self, player, x, y):
        tank_rect = player.tank.tank_rect.copy()
        tank_rect.x = x
        tank_rect.y = y

        # Kiểm tra với từng ô trong bản đồ
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                if tile == '1':  # Tường
                    wall_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if tank_rect.colliderect(wall_rect):
                        return True  # Va chạm với tường
        return False  # Không có va chạm
    #check va chạm với đạn
    def check_bullet_collision(self):
        for bullet in self.bullets[:]:
            for player in self.players:
                if player.tank.tank_rect.colliderect(bullet.rect):
                    player.health -= 25
                    self.bullets.remove(bullet)
                    if player.health == 0: # hết máu thì biến mất, có thể thêm ảnh hiệu ứng hộ
                        self.players.remove(player)
                    break
    #check người thắng
    def result(self):
        if len(self.players) == 1:
            if self.players[0].id == 1:
                print()
            elif self.players[0].id == 2:
                print()
            elif self.players[0].id == 3:
                print()
            else: print()

    def run(self, window):
        self.window = window
        mixer.init()
        mixer.music.load("asset/media.mp3")
        mixer.music.set_volume(0.4)
        mixer.music.play()

        while self.running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False

            keys = pygame.key.get_pressed()
            for i, player in enumerate(self.players):
                player.handle_input(keys)
                if keys[player.controls['shoot']]:
                    if len(self.bullets) < 4 and current_time - self.last_shot_time[i] >= self.bullet_time:
                        bullet = Bullet(player.tank.tank_rect.centerx + 25 * math.cos(math.radians(player.tank.tank_angle)),
                                        player.tank.tank_rect.centery - 25 * math.sin(math.radians(player.tank.tank_angle)),
                                        player.tank.tank_angle)
                        self.bullets.append(bullet)
                        self.last_shot_time[i] = current_time
                        self.bullet_sound.play()

                #vị trí mới tạm thời cho xe tăng
                new_x = int(player.tank.tank_x)
                new_y = int(player.tank.tank_y)
                new_angle = player.tank.tank_angle

                #check va chạm với tường
                if self.check_collision_with_walls(player, new_x, new_y):
                    # Nếu có va chạm, không cho phép di chuyển, giữ nguyên vị trí cũ
                    player.tank.tank_x = player.last_valid_x
                    player.tank.tank_y = player.last_valid_y
                else:
                    #không có va chạm, cập nhật vị trí hợp lệ
                    player.last_valid_x = new_x
                    player.last_valid_y = new_y
                    player.last_valid_angle = new_angle
                    player.tank.tank_rect.x = new_x
                    player.tank.tank_rect.y = new_y

            self.check_bullet_collision()

            self.window.fill((255, 255, 255))
            draw_map(self.window, self.map_data, TILE_SIZE)

            for player in self.players:
                player.draw(self.window)
                player.draw_health_bar(self.window)

            for bullet in self.bullets[:]:
                bullet.move()
                if bullet.is_expired_bullet():
                    explosion = Explosion(bullet.rect.centerx, bullet.rect.centery, "asset/explosion 1.png", 256, 256)
                    self.explosions_bull.append(explosion)
                    self.bullets.remove(bullet)
                else:
                    bullet.draw(self.window)

            for explosion in self.explosions_bull[:]:
                explosion.update()
                explosion.draw(self.window)
                if explosion.image is None:
                    self.explosions_bull.remove(explosion)

            pygame.display.flip()

        pygame.quit()

# Constants
TILE_SIZE = 16

def read_map(file_path):
    with open(file_path, 'r') as file:
        map_data = [line.strip() for line in file]
    return map_data

def draw_map(window, map_data, tile_size):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':
                color = (0, 0, 0)
            elif tile == '0':
                color = (255, 255, 255)
            elif tile == '*':
                color = (0, 0, 255)
            elif tile == '-':
                color = (255, 0, 0)
            else:
                continue
            pygame.draw.rect(window, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))