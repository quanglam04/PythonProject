import pygame
from pygame import mixer
from tank import Tank
from tank_control import TankControl

class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width #doan nay kich co man hinh ae biet roi
        self.window_height = window_height
        self.window = None
        self.running = True #is_running con chay hay khong !?

        self.tank = Tank("asset/Blue Tank.png", window_width, window_height)# day goi ra class Tank o tank.py
        self.control = TankControl(self.tank, window_width, window_height) #goi ra class Tankcontrol o tank_control

    def run(self, window):
        self.window = window #truyen vao gia tri cua cua so choi game
        image = pygame.image.load('asset/battlefield.png') #load background
        scaled_image = pygame.transform.scale(image, (self.window_width, self.window_height)) #scale background
        imagerect = scaled_image.get_rect()# doan nay toi chua ro ham lam vi huy viet

        # Cai dat am thanh
        mixer.init()
        mixer.music.load("asset/media.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Dieu khien
            self.control.handle_input() #goi den phuong thuc trong class Tankcontrol dung de dieu khien xe nhan input dieu khien tu ban phim

            #  Cap nhat vi tri voi tank_rect.x hoac .y (o day la vi tri hien tai cua chiec xe ve ngang va rong va ttam)
            # Nhu da noi o tren ta de tam tank_x va tank_y vi no co the dc sang so float con cai .x .y thi mac dinh la int (doan nay cap nhat hinh anh vi tri cua xe tang xuyen suot qua trinh choi game )
            self.tank.tank_rect.x = int(self.tank.tank_x) #chuyen doi sang so nguyen vi trong pygame toa do la mot int
            self.tank.tank_rect.y = int(self.tank.tank_y) #tuong tu
            #self.tank.tank_rect.clamp_ip(self.window.get_rect()) dung xoa nhe loi day :v toi test mong ae thong cam dung xoa

            # ham transform trong pygame ho tro vc chuyen doi hinh anh roate la mot ham dc viet ngay trong day co vc giup chuyen doi hinh anh xoay
            rotated_tank = pygame.transform.rotate(self.tank.tank_image, self.tank.tank_angle)
            #ham get_rect thuc chat de lay dc vi tri trung tam cua diem anh, de phuc vu cho ham blit,
            new_rect = rotated_tank.get_rect(center=self.tank.tank_rect.center) # lay lai vi tri toa do ttam moi cua xe tang khi da xoay

            #ham blit nay thuoc cua window trong pygame giup ta tao ra vi tri cua hinh anh moi voi dieu kien cho biet day du thong tin cua buc anh trong truong hop nay background cung can duoc ve lien tuc
            self.window.blit(scaled_image, imagerect) #nay lien quan den background !???
            self.window.blit(rotated_tank, new_rect) #nay scale hinh anh cua xe tang
            pygame.display.flip()

        pygame.quit()