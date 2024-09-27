import pygame
# from StartScreen import result
# import Setting
import math
class Tank:
    def __init__(self, image_path,pos):
        self.tank_image = pygame.image.load(image_path) # load hinh anh cua xe tang
        self.tank_image=pygame.transform.smoothscale(self.tank_image,(45,30))
        #get_rect co 3 gia tri la x y va center tank_rect.x goi ra chieu ngan cua xe con .y chieu doc .center la vi tri trung tam
        self.tank_rect = self.tank_image.get_rect() # cho biet chieu ngang, rong cua xe tang va lay vi tri hien tai cua xe tang
        self.tank_width, self.tank_height = self.tank_rect.size # tank_rect.size cho biet kich co cua buc anh
        self.tank_x,self.tank_y = pos # cai dat vi tri cua xe tang (vi tri ben trai cung khi ve xe tang)
        self.tank_angle = 0  # goc quay cua xe tang
        self.tank_speed = 0.79 #van toc
        self.health=100
        self.health_bar_width, self.health_bar_height=40,5


def load_map(random_index):
        with open(f'MAP/map{random_index}.txt', 'r') as f:
            map_data=[list(line.strip()) for line in f]
        spawn_points=[]
        for i in range (len(map_data)):
                for j in range (len(map_data[i])):
                    if map_data[i][j]=='*':
                        spawn_points.append( ((j * 16), (i * 16)) )
        return spawn_points
def draw_health_bar(self, window):
        # Tạo hình ảnh thanh máu
        health_bar_surface = pygame.Surface((self.health_bar_width, self.health_bar_height))
        health_bar_surface.set_colorkey((0, 0, 0))  # đặt màu đen là màu trong suốt
        health_bar_surface.fill((255, 0, 0))  # Màu đỏ cho thanh máu
        pygame.draw.rect(health_bar_surface, (0, 255, 0),
            (0, 0, int(self.health_bar_width * (self.health / 100)), self.health_bar_height))

        # Xoay thanh máu theo xe tank
        rotated_health_bar = pygame.transform.rotate(health_bar_surface, self.tank_angle)

        offset_x = -2
        offset_y = -self.tank_rect.height // 2 - 10

        # Tính toán vị trí theo xe tank
        rad_angle = math.radians(-self.tank_angle)
        rotated_offset_x = offset_x * math.cos(rad_angle) - offset_y * math.sin(rad_angle)
        rotated_offset_y = offset_x * math.sin(rad_angle) + offset_y * math.cos(rad_angle)

        bar_x = self.tank_rect.centerx + rotated_offset_x
        bar_y = self.tank_rect.centery + rotated_offset_y

        # Lấy vị trí mới của hình ảnh sau khi xoay
        rotated_rect = rotated_health_bar.get_rect(center=(bar_x, bar_y))

        # Vẽ tại vị trí mới
        window.blit(rotated_health_bar, rotated_rect.topleft)

