import pygame
import math



class LaserAiming:
    def __init__(self, x, y, angle, screen_width, screen_height, map_data):
        """self.x - self.y : toa do xe tank"""
        self.x = x
        self.y = y
        self.angle = angle
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_data = map_data    # Data of map (0 and 1)
        self.tile_size = 16     # Size of each tile in map
        self.active = False  # Status of the laser aiming
        self.remaining_length = 5
        self.end_x = 0
        self.end_y = 0
        self.normal = [0, 0]


    def calculate_end_point(self, collision_map):  # Đã gộp chung với đoạn va chạm tường
        """ Tính toán điểm kết thúc của đoạn tia laser dựa trên góc và độ dài """
        self.end_x = self.x + 10000 * math.cos(math.radians(self.angle))
        self.end_y = self.y + 10000* math.sin(math.radians(self.angle))
        line_length = 999999999
        temp_min = []
        for i in collision_map:
            line = i.clipline(self.x, self.y, self.end_x, self.end_y)
            if line:
                length = (line[0][0] - self.x) ** 2 + (line[0][1] - self.y) ** 2  # line[0]: collision point
                if 0 < length < line_length:
                    line_length = length
                    temp_min = line[0]
                    if line[0][0] == i.x:
                        self.normal = [-1, 0]
                    elif abs(line[0][0] - i.x - i.width) <= 1.5:
                        self.normal = [1, 0]
                    elif line[0][1] == i.y:
                        self.normal = [0, -1]
                    elif abs(line[0][1] - i.y - i.height) <= 1.5:
                        self.normal = [0, 1]
        if temp_min:
            self.end_x = temp_min[0]
            self.end_y = temp_min[1]
        # self.remaining_length -= math.sqrt((self.end_x - self.x) ** 2 + (self.end_y - self.y) ** 2)
        self.remaining_length -=1

    def update(self, tank_x, tank_y, tank_angle):
        # Cập nhật vị trí và góc của laser khi xe tăng thay đổi
        self.x = tank_x
        self.y = tank_y
        self.angle = 360 - tank_angle

    def draw_2_line(self, window,color):
        pygame.draw.line(window, color, [self.x, self.y], [self.end_x, self.end_y], 1)





