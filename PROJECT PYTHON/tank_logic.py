import math
import pygame


class TankLogic:
    @staticmethod
    def move_tank(tank, speed, window_width, window_height):
        rad_angle = math.radians(tank.tank_angle) # chuyen doi goc quay sang radian vi ham trong python lam vc voi radian
        dx = speed * math.cos(rad_angle) # doan nay ae ve hinh nhe :V
        dy = -speed * math.sin(rad_angle)  # a dau tru la boi khi di len tren thi Y giam

        #sao phai chia ra tank_x tank_y ma khong lay luon tank_rect.x vi don gian mot cai no luoon la kieu int con cai con loai thi tuy thich, nen neu muon chuan xac va ay thi ta dung tank_x tuong trung cho tank_rect.x
        #dieu nay giup chuyen dong tro nen muot ma hon
        tank.tank_x = max(0, min(tank.tank_x + dx, window_width - tank.tank_width)) # doan lay min la de khogn bi phong xe ra ngoai nhe
        tank.tank_y = max(0, min(tank.tank_y + dy, window_height - tank.tank_height))

    @staticmethod
    def rotate_tank(tank, angle): #quay xe tang
        tank.tank_angle = (tank.tank_angle + angle) % 360
    @staticmethod
    def check_collision(tank, bullet):
        r=bullet.image.get_width() / 2
        x,y=tank.tank_rect.center
        alpha=tank.tank_angle
        a,b=bullet.rect.center
        w,h=tank.tank_width,tank.tank_height
        check_x,check_y= a-x,b-y
        new_x=check_x*math.cos(math.radians(alpha))+check_y*math.sin(math.radians(alpha))
        new_y=check_y*math.cos(math.radians(alpha))-check_x*math.sin(math.radians(alpha))
        if -w/2<=new_x+r<=w/2 and -h/2<=new_y+r<=h/2:
            return True
        else:
            return False

    @staticmethod
    def check_collision_with_walls(tank, x, y,TILE_SIZE,map_data):
        # Kiểm tra va chạm của xe tăng với các bức tường
        tank_rect = tank.tank_rect.copy()
        tank_rect.x = x
        tank_rect.y = y
        # Kiểm tra với từng ô trong bản đồ
        for row_idx, row in enumerate(map_data):
            for col_idx, tile in enumerate(row):
                if tile == '1':
                    wall_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if tank_rect.colliderect(wall_rect):
                        return True  # Va chạm với tường
        return False  # Không có va chạm
    @staticmethod
    def check_collision_with_items(tank, x, y,TILE_SIZE,map_data):
        # Kiểm tra va chạm của xe tăng với các item
        tank_rect = tank.tank_rect.copy()
        tank_rect.x = x
        tank_rect.y = y

        # Kiểm tra với từng ô trong bản đồ
        for row_idx, row in enumerate(map_data):
            for col_idx, tile in enumerate(row):
                if tile != '1' and tile !='0' and tile != '-' and tile!='*':  # Các item
                    item_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if tank_rect.colliderect(item_rect):
                        # Xóa item khỏi map sau khi va chạm
                        map_data[row_idx][col_idx] = '0'
                        return tile
        return None
