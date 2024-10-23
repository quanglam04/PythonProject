import pygame
import math

class Laser:        #Buoc 2: Đạn laser
    def __init__(self,tank, x, y, angle):
        self.color =tank.color   # Màu của tia laser
        self.width = 5  # Độ dày của tia laser
        self.length = 10  # Chiều dài của tia laser
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1.5
        self.creation_time = pygame.time.get_ticks()
        self.bounces = 0  # Số lần có thể phản xạ (nảy) trước khi biến mất
        self.normal = [0, 0]

        self.j=0
        self.i=1
        self.end_points=tank.laser_endpoints

        #Tính toán vector hướng dựa theo góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

        self.start_x=x
        self.start_y=y

        #Toa do diem cuoi cua dan laser
        self.end_x = 0
        self.end_y = 0
        self.check = False
        self.start_time=0

    def draw(self, window):
        pygame.draw.line(window, self.color, [self.x, self.y], [self.end_x, self.end_y], self.width)

    def is_expired_bullet(self):
        # Tia laser hết hiệu lực nếu số lần phản xạ đã hết
        return self.i >5 and self.j ==4


    def laser_move(self):
        if pygame.time.get_ticks() - self.start_time >= 10:
            if self.i > 5:
                self.i =self.i-5
                self.j +=1
                self.start_x,self.start_y=self.end_points[self.j-1]
            if self.end_x and self.end_y:
                self.x=self.end_x
                self.y=self.end_y
            print(self.i,self.j)
            self.end_x= ((self.start_x*(5-self.i))  +   (self.end_points[self.j][0]*self.i) )  /5
            self.end_y= ((self.start_y*(5-self.i))  +   (self.end_points[self.j][1]*self.i)  ) /5
            self.i= self.i+1
            #print(self.x,self.y,self.end_x,self.end_y)
            self.start_time = pygame.time.get_ticks()