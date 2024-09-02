import pygame
from tank_logic import TankLogic
from bullet import Bullet  #  lớp Bullet trong  file bullet.py

class TankControl:
    def __init__(self, tank, window_width, window_height):
        self.tank = tank
        self.window_width = window_width
        self.window_height = window_height
        self.bullets = []  # Danh sách để lưu trữ các viên đạn

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            TankLogic.move_tank(self.tank, self.tank.tank_speed, self.window_width, self.window_height)
        if keys[pygame.K_s]:
            TankLogic.move_tank(self.tank, -self.tank.tank_speed, self.window_width, self.window_height)
        if keys[pygame.K_a]:
            TankLogic.rotate_tank(self.tank, 0.7)
        if keys[pygame.K_d]:
            TankLogic.rotate_tank(self.tank, -0.7)
        if keys[pygame.K_SPACE]:  # Kiểm tra nếu phím SPACE được nhấn
            self.shoot_bullet()

    def shoot_bullet(self):
        # Tạo một viên đạn mới từ vị trí của nòng súng của xe tăng
        bullet = Bullet(self.tank.rect.centerx, self.tank.rect.top)
        self.bullets.append(bullet)

    def update_bullets(self, screen):
        # Di chuyển và vẽ các viên đạn
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(screen)
            # Loại bỏ viên đạn nếu nó ra khỏi màn hình
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
