
import pygame
import math
import numpy as np


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
        self.active = True  # Status of the laser aiming
        self.remaining_length = 500
        self.end_x = 0
        self.end_y = 0
        self.normal = [0, 0]
        self.collision_map = []

        map_test = np.copy(map_data)
        # 4 buc tuong xung quanh
        self.collision_map.append(pygame.Rect( 0 *16, 0* 16, 16, 16 * 43))
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

    # Turn on, turn off the Laser
    def turn_on_Laser(self):
        self.active = True

    def turn_off_Laser(self):
        self.active = False

    def calculate_end_point(self):  # Đã gộp chung với đoạn va chạm tường
        """ Tính toán điểm kết thúc của đoạn tia laser dựa trên góc và độ dài """
        self.end_x = self.x + 1000 * math.cos(math.radians(self.angle))
        self.end_y = self.y + 1000 * math.sin(math.radians(self.angle))
        line_length = 9999999999
        temp_min = []
        for i in self.collision_map:
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
        self.remaining_length -= math.sqrt((self.end_x - self.x) ** 2 + (self.end_y - self.y) ** 2)

    def update(self, tank_x, tank_y, tank_angle):
        # Cập nhật vị trí và góc của laser khi xe tăng thay đổi
        self.x = tank_x
        self.y = tank_y
        self.angle = 360 - tank_angle

    # Vẽ đoạn tia laser (dash_length) nối giữa 2 điểm
    """Note: line_start = (x1, y1)
              line_end = (x2, y2)"""

    def draw_2_line(self, window):
        pygame.draw.line(window, (255, 0, 0), [self.x, self.y], [self.end_x, self.end_y], 2)





