import pygame

class Tank:
    def __init__(self, image_path, window_width, window_height):
        self.tank_image = pygame.image.load(image_path) # load hinh anh cua xe tang
        #get_rect co 3 gia tri la x y va center tank_rect.x goi ra chieu ngan cua xe con .y chieu doc .center la vi tri trung tam
        self.tank_rect = self.tank_image.get_rect() # cho biet chieu ngang, rong cua xe tang va lay vi tri hien tai cua xe tang
        self.tank_width, self.tank_height = self.tank_rect.size # tank_rect.size cho biet kich co cua buc anh
        self.tank_x = window_width // 2 - self.tank_width // 2 # cai dat vi tri cua xe tang theo chieu ngang
        self.tank_y = window_height // 2 - self.tank_height // 2# cai dat vi tri xe tang theo chieu doc
        self.tank_angle = 0  # goc quay cua xe tang
        self.tank_speed = 1 #van toc
    #test
    def draw(self, screen):
        screen.blit(self.tank_image, self.tank_rect)