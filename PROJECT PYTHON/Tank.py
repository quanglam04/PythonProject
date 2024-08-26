import math
import pygame
class TankGame:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = None
        self.running = True

        self.tank_image = pygame.image.load("asset/Blue Tank.png")
        self.tank_rect = self.tank_image.get_rect()
        self.tank_width, self.tank_height = self.tank_rect.size
        self.tank_speed = 0.1
        self.tank_angle = 0  # xe dang dat nam ngang

        # Use floats for more precise positioning
        self.tank_x = self.window_width // 2 - self.tank_width // 2
        self.tank_y = self.window_height // 2 - self.tank_height // 2

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
                self.rotate_tank(-0.5)
            if keys[pygame.K_d]:
                self.rotate_tank(0.5)

            # cap nhat vi tri xe tang
            self.tank_rect.x = int(self.tank_x)
            self.tank_rect.y = int(self.tank_y)
            self.tank_rect.clamp_ip(self.window.get_rect())

            self.window.fill((0, 0, 0))
            rotated_tank = pygame.transform.rotate(self.tank_image, self.tank_angle)
            new_rect = rotated_tank.get_rect(center=self.tank_rect.center)
            self.window.blit(rotated_tank, new_rect)
            pygame.display.flip()

        pygame.quit()

    def move_tank(self, speed):
        rad_angle = math.radians(self.tank_angle)
        dx = speed * math.cos(rad_angle)
        dy = -speed * math.sin(rad_angle)  # so am vi di len thi toa do y giam

        self.tank_x = max(0, min(self.tank_x + dx, self.window_width - self.tank_width))
        self.tank_y = max(0, min(self.tank_y + dy, self.window_height - self.tank_height))

    def rotate_tank(self, angle):
        self.tank_angle = (self.tank_angle + angle) % 360
