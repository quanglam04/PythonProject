import math

class TankLogic:
    @staticmethod
    def move_tank(tank, speed, window_width, window_height):
        rad_angle = math.radians(tank.tank_angle) # chuyen doi goc quay sang radian vi ham trong python lam vc voi radian
        dx = speed * math.cos(rad_angle) # doan nay ae ve hinh nhe :V
        dy = -speed * math.sin(rad_angle)  # a dau tru la boi khi di len tren thi Y giam

        #sao phai chia ra tank_x tank_y ma khong lay luon tank_rect.x vi don gian mot cai no luoon la kieu int con cai con loai thi tuy thich, nen neu muon chuan xac va ay thi ta dung tank_x tuong trung cho tank_rect.x
        #dieu nay giup chuyen dong tro nen muot ma hon
        tank.tank_x = max(0, min(tank.tank_x + dx, window_width - tank.tank_width)) # doan lay min la de khong bi phong xe ra ngoai nhe
        tank.tank_y = max(0, min(tank.tank_y + dy, window_height - tank.tank_height))

    @staticmethod
    def rotate_tank(tank, angle): #quay xe tang
        tank.tank_angle = (tank.tank_angle + angle) % 360