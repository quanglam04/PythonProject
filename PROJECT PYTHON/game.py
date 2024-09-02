import pygame
from pygame import mixer
from tank import Tank
from tank_control import TankControl
from bullet import Bullet
import sys

class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True

        self.tank = Tank("C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/Blue Tank.png", window_width, window_height)
        self.control = TankControl(self.tank, window_width, window_height)

    def run(self, window):
        self.window = window
        image = pygame.image.load('C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/battlefield.png')
        scaled_image = pygame.transform.scale(image, (self.window_width, self.window_height))
        imagerect = scaled_image.get_rect()

        mixer.init()
        mixer.music.load("C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/media.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Điều khiển
            self.control.handle_input()

            # Cập nhật vị trí của tank
            self.tank.tank_rect.x = int(self.tank.tank_x)
            self.tank.tank_rect.y = int(self.tank.tank_y)

            # Xoay tank
            rotated_tank = pygame.transform.rotate(self.tank.tank_image, self.tank.tank_angle)
            new_rect = rotated_tank.get_rect(center=self.tank.tank_rect.center)

            # Xóa màn hình và vẽ background
            self.window.blit(scaled_image, imagerect)
            self.window.blit(rotated_tank, new_rect)

            # Cập nhật và vẽ các viên đạn
            self.control.update_bullets(self.window)
            
            pygame.display.flip()

        pygame.quit()
