import math
import pygame
from bullet import Bullet

# Hàm bắn đạn chùm
def shoot_bullets(x, y, angle, bullet_count, spread_angle, speed=0.5):
    bullets = []
    if bullet_count == 1:
        # Nếu chỉ bắn một viên đạn, góc chính là góc hiện tại
        bullets.append(Bullet(x, y, angle, speed))
    else:
        start_angle = angle - spread_angle / 2  # Góc bắt đầu của đạn
        for i in range(bullet_count):
            # Tính góc cho mỗi viên đạn dựa trên số lượng đạn và góc lan tỏa
            bullet_angle = start_angle + (spread_angle / (bullet_count - 1)) * i
            bullets.append(Bullet(x, y, bullet_angle, speed))
    return bullets
