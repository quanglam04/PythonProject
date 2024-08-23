import pygame
import math

class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True

        self.tank_image = pygame.image.load("asset/Blue Tank.png")
        self.tank_rect = self.tank_image.get_rect()
        self.tank_width, self.tank_height = self.tank_rect.size
        self.tank_speed = 1
        self.tank_angle = 180

        self.tank_rect.x = self.window_width // 2 - self.tank_width // 2
        self.tank_rect.y = self.window_height // 2 - self.tank_height // 2

    def run(self, window):
        self.window = window
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.move_tank(self.tank_speed)
            if keys[pygame.K_s]:
                self.move_tank(-self.tank_speed)
            if keys[pygame.K_a]:
                self.rotate_tank(-1)
            if keys[pygame.K_d]:
                self.rotate_tank(1)

            self.tank_rect.clamp_ip(self.window.get_rect())

            self.window.fill((0, 0, 0))
            rotated_tank = pygame.transform.rotate(self.tank_image, self.tank_angle)
            new_rect = rotated_tank.get_rect(center=self.tank_rect.center)
            self.window.blit(rotated_tank, new_rect)
            pygame.display.flip()

        pygame.quit()

    def move_tank(self, speed):
        x, y = self.tank_rect.topleft
        dx = speed * math.cos(math.radians(self.tank_angle))
        dy = speed * math.sin(math.radians(self.tank_angle))
        self.tank_rect.topleft = (x + dx, y + dy)

    def rotate_tank(self, angle):
        self.tank_angle += angle
        self.tank_angle %= 360