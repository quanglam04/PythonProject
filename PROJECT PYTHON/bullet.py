import pygame
import math


class Bullet:
    def __init__(self, x, y, angle, speed=0.9):
        self.image = pygame.image.load("asset/bullet.png")
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(self.image, (15, 15))  # Điều chỉnh kích thước đạn
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = speed
        self.bullet_x=self.rect.x
        self.bullet_y=self.rect.y
        self.creation_time=pygame.time.get_ticks()
        self.bounce_count = 0  # Biến đếm số lần nảy

        # Tính toán vector hướng dựa trên góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

    def move(self, map_data, tile_size):
        # Dự đoán vị trí mới của viên đạn (+ hướng di chuyển)
        new_bullet_x = self.bullet_x + self.direction_x
        new_bullet_y = self.bullet_y + self.direction_y

        # Tính toán vị trí ô trên bản đồ tương ứng với vị trí mới của viên đạn
        map_x = int(new_bullet_x / tile_size)
        map_y = int(new_bullet_y / tile_size)

        # Kiểm tra xem có va chạm với tường không
        if 0 <= map_y < len(map_data) and 0 <= map_x < len(map_data[0]):  # Kiển tra đạn trong bản đồ hay không
            if map_data[map_y][map_x] == '1':  # Ô có tường
                # Xác định cạnh của ô tường (left, right, top, bottom)
                left = map_x * tile_size
                right = left + tile_size
                top = map_y * tile_size
                bottom = top + tile_size

                # Kiểm tra va chạm với các cạnh của ô tường
                # Đây là đảo ngược hướng đạn
                if (left <= new_bullet_x <= right) and (
                        top <= new_bullet_y <= bottom):  # Kiểm tra đạn nằm tỏng phạm vị tường hay không
                    # Xác định va chạm vào cạnh nào
                    if (self.bullet_x < left and new_bullet_x >= left) or (
                            self.bullet_x > right and new_bullet_x <= right):  # Kiểm tra va vào cạnh trái hay phải không
                        self.direction_x *= -1  # Đảo ngược hướng theo trục X
                    if (self.bullet_y < top and new_bullet_y >= top) or (
                            self.bullet_y > bottom and new_bullet_y <= bottom):
                        self.direction_y *= -1  # Đảo ngược hướng theo trục Y

                    self.bounce_count += 1  # Nếu chạm đếm số lần nảy zo tường :)

        # Cập nhật vị trí của viên đạn
        self.bullet_x += self.direction_x
        self.bullet_y += self.direction_y
        self.rect.x = int(self.bullet_x)
        self.rect.y = int(self.bullet_y)

    def draw(self, window):
        rotated_bullet = pygame.transform.rotate(self.image, -self.angle)
        window.blit(rotated_bullet, self.rect)

    def is_expired_bullet(self):
        # Kiểm tra số lần nảy
        return self.bounce_count >= 5