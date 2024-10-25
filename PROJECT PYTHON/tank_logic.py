import math
import numpy as np
class TankLogic:
    @staticmethod
    def move_tank(tank, speed, window_width, window_height):
        rad_angle = math.radians(tank.tank_angle) # chuyen doi goc quay sang radian vi ham trong python lam vc voi radian
        tank.dx = speed * math.cos(rad_angle) # doan nay ae ve hinh nhe :V
        tank.dy = -speed * math.sin(rad_angle)  # a dau tru la boi khi di len tren thi Y giam

        #sao phai chia ra tank_x tank_y ma khong lay luon tank_rect.x vi don gian mot cai no luoon la kieu int con cai con loai thi tuy thich, nen neu muon chuan xac va ay thi ta dung tank_x tuong trung cho tank_rect.x
        #dieu nay giup chuyen dong tro nen muot ma hon
        tank.tank_x = max(0, min(tank.tank_x + tank.dx, window_width - tank.tank_width)) # doan lay min la de khogn bi phong xe ra ngoai nhe
        tank.tank_y = max(0, min(tank.tank_y + tank.dy, window_height - tank.tank_height))
        tank.d_angle=0
        tank.check=True
    @staticmethod
    def rotate_tank(tank, angle): #quay xe tang
        tank.d_angle = angle
        tank.tank_angle = (tank.tank_angle + angle) % 360
        # tank.dx,tank.dy=0,0

    @staticmethod
    def check_in_circle(point, a, b, r):
        distance = (point[0] - a) * (point[0] - a) + (point[1] - b) * (point[1] - b)
        print(point[0], point[1], a, b)
        print(distance, r * r)
        return r * r - distance >= 0
    @staticmethod
    def calculate_rotated_corners(tank):
        top_left = (tank.tank_rect.x, tank.tank_rect.y)
        top_right = (tank.tank_rect.x + tank.tank_width, tank.tank_rect.y)
        bottom_left = (tank.tank_rect.x, tank.tank_rect.y + tank.tank_height)
        bottom_right = (tank.tank_rect.x + tank.tank_width, tank.tank_rect.y + tank.tank_height)
        cx, cy = tank.tank_rect.center
        angle_rad = math.radians(tank.tank_angle)
        rotated_top_left = (
            -(cx - top_left[0]) * math.cos(angle_rad) - (cy - top_left[1]) * math.sin(angle_rad) + cx,
            -(cy - top_left[1]) * math.cos(angle_rad) + (cx - top_left[0]) * math.sin(angle_rad) + cy
        )

        rotated_top_right = (
            -(cx - top_right[0]) * math.cos(angle_rad) - (cy - top_right[1]) * math.sin(angle_rad) + cx,
            -(cy - top_right[1]) * math.cos(angle_rad) + (cx - top_right[0]) * math.sin(angle_rad) + cy
        )

        rotated_bottom_left = (
            -(cx - bottom_left[0]) * math.cos(angle_rad) - (cy - bottom_left[1]) * math.sin(angle_rad) + cx,
            -(cy - bottom_left[1]) * math.cos(angle_rad) + (cx - bottom_left[0]) * math.sin(angle_rad) + cy
        )

        rotated_bottom_right = (
            -(cx - bottom_right[0]) * math.cos(angle_rad) - (cy - bottom_right[1]) * math.sin(angle_rad) + cx,
            -(cy - bottom_right[1]) * math.cos(angle_rad) + (cx - bottom_right[0]) * math.sin(angle_rad) + cy
        )
        return [rotated_top_left, rotated_top_right, rotated_bottom_left, rotated_bottom_right]
    @staticmethod
    def check_collision(tank, bullet):
        r=bullet.radius
        x,y=tank.tank_rect.center
        alpha=float(tank.tank_angle)
        a,b=bullet.rect.center
        w,h=tank.tank_width,tank.tank_height
        check_x,check_y= a-x,b-y
        new_x=float(check_x*math.cos(math.radians(alpha))-check_y*math.sin(math.radians(alpha)))
        new_y=float(check_y*math.cos(math.radians(alpha))+check_x*math.sin(math.radians(alpha)))
        tmp = TankLogic.calculate_rotated_corners(tank)
        if max(-w / 2, new_x - r) <= min(w / 2, new_x + r) and max(-h / 2, new_y - r) <= min(h / 2, new_y + r):
            if -w / 2 <= new_x <= w / 2 or -h / 2 <= new_y <= h / 2:
                return True
            else:
                for corner in tmp:
                    if TankLogic.check_in_circle(corner, a, b, r):
                        return True
                return False
        else:
            return False

    @staticmethod
    def check_collision_with_tank(tank1,tank2):
        offset_x = tank2.tank_x - tank1.tank_x
        offset_y = tank2.tank_y - tank1.tank_y
        collision_point = tank1.tank_mask.overlap(tank2.tank_mask, (offset_x, offset_y))
        return collision_point is not None
    @staticmethod
    def check_collision_with_wall(tank,map_mask):
        offset_x=int (tank.tank_x-tank.tank_width/2)
        offset_y=int (tank.tank_y-tank.tank_height)
        check = map_mask.overlap(tank.tank_mask,(offset_x,offset_y))
        return check is not None
    @staticmethod
    def check_collision_with_items(tank, item,item_name,map_data,title_size):
        res=None
        for tmp in item:
            offset_x= int(tank.tank_x-tmp[1]-title_size)
            offset_y= int(tank.tank_y-tmp[2]-title_size)
            check=item_name[tmp[0]].overlap(tank.tank_mask,(offset_x,offset_y))
            if check is not None:
                print(item_name[tmp[0]])
                map_data[tmp[2]//title_size][tmp[1]//title_size]= '0'
                res=tmp[0]
                item.remove(tmp)
                break
        return res
    @staticmethod
    def is_on_line(x,y,A,B,C):
        d= abs(A*x+B*y+C) / math.sqrt(A*A+B*B)
        return d <0.5
    @staticmethod
    def line_from_point(p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        A = y2 - y1
        B = x1 - x2
        C = (x2 * y1 - x1 * y2)
        return A, B, C
    @staticmethod
    def distance_point(x1,y1,x2,y2):
        return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )
    @staticmethod
    def check_point_between(x1,y1,x2,y2,x3,y3):
        CA=TankLogic.distance_point(x1,y1,x2,y2)
        CB=TankLogic.distance_point(x2,y2,x3,y3)
        AB=TankLogic.distance_point(x1,y1,x3,y3)
        return CA+CB-AB<1
    @staticmethod
    def check_collision_with_laser(tank,laser):
        #phuong trinh duong thang cua laser Ax+By+C=0
        #vi du end_x=4 end_y =5 x=2 y=3
        A= laser.end_y-laser.y #2
        B= laser.x-laser.end_x # -2
        C=laser.end_x*laser.y-laser.end_y*laser.x #4*3 -5*2 =2 => 2x-2y+2=0

        #4 goc hinh chu nhat
        rects=TankLogic.calculate_rotated_corners(tank)
        for rect in rects:
            if TankLogic.check_point_between(laser.x, laser.y, rect[0], rect[1], laser.end_x, laser.end_y) :
                return rect[0],rect[1]


        res= [TankLogic.line_from_point(rects[0], rects[1]), TankLogic.line_from_point(rects[1], rects[3]),
              TankLogic.line_from_point(rects[2], rects[3]), TankLogic.line_from_point(rects[0], rects[2])]
        #lan luot la canh ben tren, canh ben phai, canh o duoi, canh ben trai

        tmp=res[0] #canh ben tren
        a = np.array([[A, B], [tmp[0], tmp[1]]])
        b = np.array([-C, -tmp[2]])
        solution = np.linalg.solve(a, b)
        x, y = solution

        if TankLogic.check_point_between(laser.x, laser.y, x, y, laser.end_x, laser.end_y) and TankLogic.check_point_between(rects[0][0],rects[0][1],x,y,rects[1][0],rects[1][1]):
            return x,y

        tmp=res[1] #canh ben phai
        a = np.array([[A, B], [tmp[0], tmp[1]]])
        b = np.array([-C, -tmp[2]])
        solution = np.linalg.solve(a, b)
        x, y = solution
        if TankLogic.check_point_between(laser.x, laser.y, x, y, laser.end_x, laser.end_y) and TankLogic.check_point_between(rects[1][0],rects[1][1],x,y,rects[3][0],rects[3][1]):
            return x,y


        tmp=res[2] #canh ben duoi
        a = np.array([[A, B], [tmp[0], tmp[1]]])
        b = np.array([-C, -tmp[2]])
        solution = np.linalg.solve(a, b)
        x, y = solution
        if TankLogic.check_point_between(laser.x, laser.y, x, y, laser.end_x, laser.end_y) and TankLogic.check_point_between(rects[2][0],rects[2][1],x,y,rects[3][0],rects[3][1]):
            return x,y


        tmp=res[3] #canh ben trai
        a = np.array([[A, B], [tmp[0], tmp[1]]])
        b = np.array([-C, -tmp[2]])
        solution = np.linalg.solve(a, b)
        x, y = solution
        if TankLogic.check_point_between(laser.x, laser.y, x, y, laser.end_x, laser.end_y) and TankLogic.check_point_between(rects[0][0],rects[0][1],x,y,rects[3][0],rects[3][1]):
            return x,y



        # for tmp in res:
        #     a=np.array([  [A,B] , [tmp[0],tmp[1]]  ])
        #     b=np.array([-C,-tmp[2]])
        #     try:
        #         solution=np.linalg.solve(a,b)
        #         x,y=solution
        #         #print(x,y,laser.x,laser.y,laser.end_x,laser.end_y)
        #         if  TankLogic.check_point_between(laser.x,laser.y,x,y,laser.end_x,laser.end_y):
        #             print(A,B,C,tmp[0],tmp[1],tmp[2],"diem: " ,x,y,laser.x,laser.y,laser.end_x,laser.end_y )
        #             print(res)
        #             print(A, B, C)
        #             return True
        #     except np.linalg.LinAlgError:
        #         pass

        return None,None

