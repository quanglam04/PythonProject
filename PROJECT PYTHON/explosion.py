import pygame
class  Explosion:
    def __init__(self,x,y,frames,animation=1000):
        self.frames=frames
        self.animation = animation
        self.current_frame=0
        self.image=self.frames[self.current_frame]
        self.rect=self.image.get_rect(center=(x,y))
        self.start_time=pygame.time.get_ticks()

    def update(self):
        elapsed_time=pygame.time.get_ticks()-self.start_time #tong thoi gian ma da chay khi dc goi den ham update
        if elapsed_time<self.animation: #cho animation chay khong qua animation giay
            self.current_frame=(elapsed_time //(self.animation//len(self.frames)) ) %len(self.frames) #chia ra xem la thoi diem nao ung voi khung hinh nao
            self.image=self.frames[self.current_frame] #cap nhat hinh anh
        else:
            self.image=None

    def draw(self,surface):
        if self.image is not None: #ve
            surface.blit(self.image,self.rect)


class Animation(Explosion):
    def __init__(self, x,y,frames,angle,animation=1000):
        super().__init__( x,y,frames, animation=1000)
        self.angle=angle
    def draw(self, surface):
        if self.image is not None:
            self.image=pygame.transform.smoothscale(self.image,(128,128))
            # Xoay hình ảnh theo góc của Animation
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect = rotated_image.get_rect(center=self.rect.center)
            surface.blit(rotated_image, new_rect)

