import pygame
import math
from Static_object import beams

class Beam:
    def __init__(self, tank, x, y):
        self.tank = tank
        self.x = x
        self.y = y
        # Tải hình ảnh tia laser
        self.image=beams[tank.id][0]
        self.rect = self.image.get_rect(center=(x, y))
        # Lưu trữ thời gian bắt đầu
        self.start_time = pygame.time.get_ticks()
        self.current_frame=0
        self.last_time_frame=0
        self.end_x , self.end_y = 0,0
        self.dame=40
    def draw(self, window):
        # Xoay hình ảnh theo góc của xe tăng
        if pygame.time.get_ticks()-self.last_time_frame >50:
            self.current_frame +=1
            self.last_time_frame=pygame.time.get_ticks()
        if self.current_frame ==3:
            self.current_frame =0
        rotated_image = pygame.transform.rotate(beams[self.tank.id][self.current_frame], self.tank.tank_angle)
        # Lấy hình chữ nhật của hình ảnh sau khi xoay
        rect = rotated_image.get_rect()
        # Tính toán vị trí đầu súng (điểm phát tia)
        # Căn chỉnh rect để điểm đầu của tia trùng với đầu súng

        rect.center =(self.tank.tank_rect.centerx + 273 * math.cos(math.radians(self.tank.tank_angle)),
                            self.tank.tank_rect.centery - 273 * math.sin(math.radians(self.tank.tank_angle)))

        # Vẽ hình ảnh lên cửa sổ
        window.blit(rotated_image, rect)

    def is_expired(self):
        # Kiểm tra xem hình chữ nhật đã tồn tại đủ 3.5 giây hay chưa
        return pygame.time.get_ticks() - self.start_time > 3000
    def update_end_point(self):
        self.x=self.tank.tank_rect.centerx
        self.y=self.tank.tank_rect.centery
        self.end_x = self.x + 523 * math.cos(math.radians(360-self.tank.tank_angle))
        self.end_y = self.y + 523 * math.sin(math.radians(360-self.tank.tank_angle))


