import pygame
import math

'''
Dan laser: ban nhu dan thuong, nhung voi toc do nhanh hon rat nhieu, voi hinh anh tia laser
Có 1 đường laser để ngắm bắn trước, không phụ thuộc vào số lần phản xạ, mà phụ thuộc vào độ dài tia laser.
Những việc cần làm:
+ Tạo ra 1 đường laser ngắm bắn: tồn tại liên tục trong 30s
    + Góc di chuyển theo góc xe tăng
    + Phản xạ như đạn nảy
    + Độ dài: ?? (pixel) 
    + Gặp tường thì phản xạ. Gặp tank thì ngừng.
+ Bắn đạn laser:
    + Y hệt đạn nảy, nhưng hình ảnh khác
    + Tốc độ nhanh hơn nhiều 
'''
class Laser:        #Buoc 2: Đạn laser
    def __init__(self, x, y, angle):
        self.color = (255, 0, 0)  # Màu của tia laser
        self.width = 4  # Độ dày của tia laser
        self.length = 30  # Chiều dài của tia laser
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1.5
        self.creation_time = pygame.time.get_ticks()
        self.bounces = 0  # Số lần có thể phản xạ (nảy) trước khi biến mất

        #Tính toán vector hướng dựa theo góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

    def move(self, map_data, tile_size):
        #Dự đoán vị trí mới của viên đạn (+hướng di chuyển)
        new_bullet_x = self.x + self.direction_x
        new_bullet_y = self.y + self.direction_y

        #Tính toán vị trí ô trên bản đồ ứng với vị trí mới của viên đạn
        map_x = int(new_bullet_x / tile_size)
        map_y = int(new_bullet_y / tile_size)

        #Kiểm tra xem có va chạm với tường không
        if 0 <= map_y < len(map_data) and 0 <= map_x < len(map_data[0]):
            if map_data[map_y][map_x] == '1':       #Ô có tường
                left = map_x*tile_size
                right = left + tile_size
                top = map_y * tile_size
                bottom = top + tile_size

                #Kiểm tra va chạm với các cạnh của tường  == Đảo ngược hướng đạn

                if(left <= new_bullet_x <= right) and (top <= new_bullet_y <= bottom):
                    if (self.x < left and new_bullet_x >= left) or (self.x > right and new_bullet_x <= right):
                        self.direction_x *= -1      #Đảo ngược theo chiều trục X
                        self.angle = 180 - self.angle
                    if (self.y < top and new_bullet_y >= top) or (self.y > bottom and new_bullet_y <= bottom):
                        self.direction_y *= -1      #Đảo ngược theo chiều trục Y
                        self.angle = -self.angle

                    self.bounces += 1

        #Cập nhật vị trí của viên đạn
        self.x += self.direction_x
        self.y += self.direction_y

    def draw(self, window):
        # Tính toán điểm kết thúc của tia laser
        end_x = self.x + self.length * math.cos(math.radians(self.angle))
        end_y = self.y - self.length * math.sin(math.radians(self.angle))

        # Vẽ tia laser
        pygame.draw.line(window, self.color, (self.x, self.y), (end_x, end_y), self.width)

    def is_expired_bullet(self):
        # Tia laser hết hiệu lực nếu số lần phản xạ đã hết
        return self.bounces >= 6
