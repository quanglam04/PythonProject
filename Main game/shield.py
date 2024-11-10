import pygame.time

from Static_object import shield_frames as sfs
class Shield:
    def __init__(self,tank):
        self.speed=5
        self.tank=tank
        self.x=tank.tank_rect.x
        self.y=tank.tank_rect.y
        self.image=sfs[0]
        self.current_frame=0
        self.time_display=pygame.time.get_ticks()
        self.animation =400
    def update_pos(self):
        self.x=self.tank.tank_rect.x
        self.y=self.tank.tank_rect.y
    def draw(self,window):
        window.blit(sfs[self.current_frame],(self.x-45,self.y-45))
        if pygame.time.get_ticks()-self.time_display >20:
            self.current_frame +=1
            self.time_display=pygame.time.get_ticks()
        if self.current_frame >= len(sfs):
            self.current_frame=0
