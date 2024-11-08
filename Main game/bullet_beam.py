import pygame
import math

class Beam:
    def __init__(self, tank, x, y, angle):
        self.tank = tank
        self.color = tank.color
        self.x = x
        self.y = y
        self.angle = angle
        # Tải hình ảnh tia laser
        self.colortank = "Blue"
        if self.color == (255, 0, 0) :
            self.colortank = "Red"
        if self.color == (255,165,0) :
            self.colortank = "Orange"
        if self.color == (0, 255, 0) :
            self.colortank = "Green"
        bimg = "C:/Users/84334/Desktop/python/PythonProject/Main game/asset/Beam/" + self.colortank + " Beam1.png"
        self.image = pygame.image.load(bimg)

        self.rect = self.image.get_rect(center=(x, y))

        # Lưu trữ thời gian bắt đầu
        self.start_time = pygame.time.get_ticks()

    def draw(self, window):
        # Xoay hình ảnh theo góc của xe tăng
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        
        # Lấy hình chữ nhật của hình ảnh sau khi xoay
        rect = rotated_image.get_rect()
        
        # Tính toán vị trí đầu súng (điểm phát tia)
        offset_x = math.cos(math.radians(-self.angle)) * self.rect.width / 2
        offset_y = math.sin(math.radians(-self.angle)) * self.rect.width / 2
        
        # Căn chỉnh rect để điểm đầu của tia trùng với đầu súng
        rect.center = (self.x + offset_x, self.y + offset_y)

        # Vẽ hình ảnh lên cửa sổ
        window.blit(rotated_image, rect)

    def is_expired(self):
        # Kiểm tra xem hình chữ nhật đã tồn tại đủ 3.5 giây hay chưa
        return pygame.time.get_ticks() - self.start_time > 3500
    
    def dame(self):
        if self.tank.dame_bonus != 0:
            return 2
        return 1
   