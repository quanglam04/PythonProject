import pygame
import math
'''
Có 1 đường laser để ngắm bắn trước, không phụ thuộc vào số lần phản xạ, mà phụ thuộc vào độ dài tia laser.
Những việc cần làm:
+ Tạo ra 1 đường laser ngắm bắn: tồn tại liên tục trong 30s
    + Góc di chuyển theo góc xe tăng
    + Phản xạ như đạn nảy
    + Độ dài: ?? (pixel) 
    + Gặp tường thì phản xạ. Gặp tank thì ngừng.
     
    ?Xem xet xem dan laser duoc ban bao nhieu lan or bao nhieu lau?
    
'''



class LaserAiming:
    def __init__(self, x, y, angle, screen_width, screen_height, length=500, dash_length=10, gap_length=5):
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length  # Độ dài đường laser
        self.dash_length = dash_length  # Độ dài nét đứt
        self.gap_length = gap_length  # Khoảng cách giữa các nét đứt
        self.end_x, self.end_y = self.calculate_end_point()

        self.active = True  # Trạng thái của laser ngắm, tắt khi bắn
        self.screen_width = screen_width
        self.screen_height = screen_height

    def calculate_end_point(self):
        """ Tính toán điểm kết thúc của đường laser dựa trên góc và độ dài """
        end_x = self.x + self.length * math.cos(math.radians(self.angle))
        end_y = self.y - self.length * math.sin(math.radians(self.angle))
        return end_x, end_y

    def draw(self, window):
        """ Vẽ đường laser nét đứt """
        if not self.active:  # Nếu laser tắt, không vẽ nữa
            return

        start_x = self.x
        start_y = self.y
        end_x, end_y = self.end_x, self.end_y

        dx = end_x - start_x
        dy = end_y - start_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        direction_x = dx / distance
        direction_y = dy / distance

        total_drawn = 0
        while total_drawn < distance:
            segment_start_x = start_x + direction_x * total_drawn
            segment_start_y = start_y + direction_y * total_drawn
            segment_end_x = start_x + direction_x * min(total_drawn + self.dash_length, distance)
            segment_end_y = start_y + direction_y * min(total_drawn + self.dash_length, distance)

            pygame.draw.line(window, (255, 0, 0), (segment_start_x, segment_start_y), (segment_end_x, segment_end_y), 2)

            total_drawn += self.dash_length + self.gap_length

    def update(self, tank_x, tank_y, tank_angle):
        """ Cập nhật vị trí và góc của laser khi xe tăng thay đổi """
        self.x = tank_x
        self.y = tank_y
        self.angle = tank_angle
        self.end_x, self.end_y = self.calculate_end_point()

    def shoot(self):
        """ Tắt laser khi bắn """
        self.active = False

    def reflect(self):
        """ Xử lý phản xạ khi laser gặp tường """
        if self.end_x <= 0 or self.end_x >= self.screen_width:  # Phản xạ theo chiều ngang
            self.angle = 180 - self.angle
        if self.end_y <= 0 or self.end_y >= self.screen_height:  # Phản xạ theo chiều dọc
            self.angle = -self.angle
        self.end_x, self.end_y = self.calculate_end_point()  # Cập nhật lại điểm kết thúc sau khi phản xạ