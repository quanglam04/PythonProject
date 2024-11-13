import pygame
class  Explosion:
    def __init__(self,x,y,frames,animation):
        self.frames=frames
        self.animation = animation
        self.current_frame=0
        self.image=self.frames[self.current_frame]
        self.rect=self.image.get_rect(center=(x,y))
        self.start_time=pygame.time.get_ticks()

    def update(self):
        elapsed_time=pygame.time.get_ticks()-self.start_time #tong thoi gian ma da chay khi dc goi den ham update
        if elapsed_time<self.animation: #cho animation chay khong qua animation giay
            self.current_frame=(elapsed_time //(self.animation//len(self.frames)) )  #chia ra xem la thoi diem nao ung voi khung hinh nao
            if self.current_frame >= len(self.frames):
                self.current_frame= len(self.frames)-1
            self.image=self.frames[self.current_frame] #cap nhat hinh anh
        else:
            self.image=None

    def draw(self,surface):
        if self.image is not None: #ve
            surface.blit(self.image,self.rect)


class Animation(Explosion):
    def __init__(self, x,y,frames,angle,new_w,new_h,animation):
        super().__init__( x,y,frames, animation)
        self.angle=angle
        self.new_w=new_w
        self.new_h=new_h
    def draw(self, surface):
        if self.image is not None:
            self.image=pygame.transform.smoothscale(self.image,(self.new_w,self.new_h))
            # Xoay hình ảnh theo góc của Animation
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect = rotated_image.get_rect(center=self.rect.center)
            surface.blit(rotated_image, new_rect)

