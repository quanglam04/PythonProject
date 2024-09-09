import pygame

class  Explosion:

    def __init__(self,x,y,sheet_path,frame_width,frame_height,animation=1000):
        self.sheet_path=pygame.image.load(sheet_path).convert_alpha() #nghe don lam cho hinh anh muot ma hon
        self.frame_width=frame_width
        self.frame_height=frame_height

        self.frames=[] #call ra cac khung hinh
        total_frame=self.sheet_path.get_width() // self.frame_width #tong con bao nhieu khung hinh tren hang (cai nay lay 1 hang thoi cho do lau)

        for i in range(total_frame):
            frame=self.sheet_path.subsurface(i*self.frame_width,0,self.frame_width,self.frame_height) # tham so (x,y,cr cua anh, cdai cua anh) lay 1 hang => y mac dinh=0
            self.frames.append(frame)

        self.current_frame=0
        self.image=self.frames[self.current_frame]
        self.rect=self.image.get_rect(center=(x,y))
        self.animation=animation
        self.start_time=pygame.time.get_ticks() #cap nhat thoi diem animation bat dau dc goi den

    def update(self):
        elapsed_time=pygame.time.get_ticks()-self.start_time #tong thoi gian ma da chay khi dc goi den ham update
        if elapsed_time<self.animation: #cho animation chay khong qua animation giay
            self.current_frame=(elapsed_time //(self.animation//len(self.frames)) ) %len(self.frames) #chia ra xem la thoi diem nao ung voi khung hinh nao
            self.image=self.frames[self.current_frame] #cap nhat hinh anh

        else:
            self.image=None



    def draw(self,surface):
        if self.image is not None: #ve
            surface.blit(self.image, self.rect)


