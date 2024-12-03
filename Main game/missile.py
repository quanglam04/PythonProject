from explosion import Explosion
from AI import pathfinder
import pygame
import Setting
import math
import Static_object
from Sound import missile_tracking_sound as mts
class Missile:
    def __init__(self,tank,x,y,angle):
        self.tank=tank
        self.angle=angle
        self.x=x
        self.y=y
        self.create_x,self.create_y=x,y
        self.img= Static_object.missile_image
        self.img_rect=self.img.get_rect()
        self.img_rect.x,self.img_rect.y=int(self.x),int(self.y)
        self.start_point=pathfinder.Node(int (self.y/Setting.tile_size),int (self.x/Setting.tile_size))
        self.end_point=pathfinder.Node(1,1)
        self.speed=Setting.missile_speed
        self.path=None
        self.change=False
        self.last_end=pathfinder.Node(1,1)
        self.last_update=pygame.time.get_ticks()
        self.target=None
        self.dame=30
        self.last_smoke_frame_time=0
        self.last_sound_time=0
    def draw(self,window):
        self.img_rect.x,self.img_rect.y= int(self.x), int(self.y)
        rotate_img=pygame.transform.rotate(self.img,self.angle)
        new_rect=rotate_img.get_rect(center=self.img_rect.center)
        window.blit(rotate_img,new_rect)
    def create_smoke_fame(self):
        if pygame.time.get_ticks()-self.last_smoke_frame_time >100:
            if self.target is not None:
                explosion = Explosion(self.img_rect.centerx - 15 * math.cos(math.radians(self.angle)),
                                      self.img_rect.centery + 15 * math.sin(math.radians(self.angle)),
                                      Static_object.smoke_tanks_frames[self.target.id], 300)
            else:
                explosion=Explosion( self.img_rect.centerx-15*math.cos(math.radians(self.angle)), self.img_rect.centery+15*math.sin(math.radians(self.angle)),Static_object.normal_smoke_frames,300)
            self.last_smoke_frame_time=pygame.time.get_ticks()
            return explosion
        return None

    def update_tank_pos(self,tanks):
        dis=math.inf
        if pygame.time.get_ticks()-self.last_update >2000:
            for tank in tanks:
                d= math.sqrt( (tank.tank_x-self.x)*(tank.tank_x-self.x) +(tank.tank_y-self.y)*(tank.tank_y-self.y) )
                if d<dis:
                    dis=d
                    self.target=tank
            self.last_update=pygame.time.get_ticks()
        #print(self.target)
        if self.target is not None:
            self.end_point=pathfinder.Node(int (self.target.tank_rect.centery/Setting.tile_size),int(self.target.tank_rect.centerx/Setting.tile_size) )
        else:
            angle_rad=math.radians(self.angle)
            dx=self.speed*math.cos(angle_rad)
            dy=-self.speed*math.sin(angle_rad)
            self.x+=dx
            self.y+=dy
            self.start_point = pathfinder.Node(int(self.y / Setting.tile_size), int(self.x / Setting.tile_size))
        if (self.end_point.x != self.last_end.x) or (self.end_point.y != self.last_end.y):
            #print("DCMM")
            self.last_end.x=self.end_point.x
            self.last_end.y=self.end_point.y
            self.change=True
        # else:
        #     self.change=False



    def missile_path(self,map_data):
        if self.change:
            self.path=pathfinder.a_star(self.start_point,self.end_point,map_data)
            self.change=False
        if self.path:
            if pygame.time.get_ticks()-self.last_sound_time >1000:
                mts.play()
                self.last_sound_time=pygame.time.get_ticks()
            #mts.play()
            self.start_point = pathfinder.Node(self.path[-1][0], self.path[-1][1])
            target_x,target_y=self.path[0][1] * Setting.tile_size, self.path[0][0] * Setting.tile_size
            dx,dy=target_x-self.x,target_y-self.y
            d=math.sqrt(dx*dx+dy*dy)
            if d:
                self.x += self.speed*dx/d
                self.y += self.speed*dy/d
                a=dx/d
                b=dy/d
                angle_radian =math.atan2(a,b)
                self.angle=math.degrees(angle_radian) - 90
                #print(self.angle)
            if abs(dx) < self.speed and abs(dy) < self.speed:
                self.x, self.y = target_x, target_y  # Snap to the exact target position
                self.path.pop(0)
        #self.start_point = pathfinder.Node(int(self.y / 16), int(self.x / 16))

    def check_collision_with_wall(self,map_data):
        a, b = self.img_rect.centerx+15*math.cos(math.radians(self.angle)), self.img_rect.centery-15*math.sin(math.radians(self.angle))

        if map_data[int(b/Setting.tile_size)][int(a/Setting.tile_size)]== '1':
            if self.angle % 90 ==0:
                self.angle=(self.angle+180)%360
            self.angle= (self.angle-30)%360
    def missile_bug_handle(self,map_data):
        if map_data[int(self.create_y/Setting.tile_size) ][int(self.create_x/Setting.tile_size)] == '1':
            return True


