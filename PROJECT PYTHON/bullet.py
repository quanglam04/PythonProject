import pygame


class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load('C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/bullet.png')  # Đường dẫn tới hình ảnh viên đạn
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 2  # Tốc độ di chuyển của đạn

    def move(self):
        self.rect.y -= self.speed  # Điều chỉnh tốc độ di chuyển của đạn

    def draw(self, window):
        window.blit(self.image, self.rect)
