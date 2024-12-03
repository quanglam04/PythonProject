import pygame.time as time
import math
from tank import Tank
from AI import pathfinder
class TankAi(Tank):
    def __init__(self,pos,i_d):
        super().__init__(pos,i_d)
        self.tank_endpoint=pathfinder.Node(1,1)
        self.tank_startpoint=pathfinder.Node(1,1)
        self.last_update=time.get_ticks()
        self.target =None
    def update_tank_pos(self,tanks):
        dis=math.inf
        if time.get_ticks()-self.last_update >2000:
            for tank in tanks:
                d= math.sqrt( (tank.tank_x-self.x)*(tank.tank_x-self.x) +(tank.tank_y-self.y)*(tank.tank_y-self.y) )
                if d<dis:
                    dis=d
                    self.target=tank
            self.last_update=time.get_ticks()
