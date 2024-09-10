import pygame
import sys
import button

class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 55)
        self.start_btn = button.Button(395, 185, pygame.image.load("C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/start_btn.png").convert_alpha(), 1)
        self.exit_btn = button.Button(412, 360, pygame.image.load("C:/Users/84334/Desktop/branchme/PythonProject/PROJECT PYTHON/asset/exit_btn.png").convert_alpha(), 1)

    def draw(self, screen):
        screen.fill((52, 78, 91))
        self.start_btn.draw(screen)
        self.exit_btn.draw(screen)

    def handle_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif self.start_btn.draw(screen):
                return 'start'
            elif self.exit_btn.draw(screen):
                return 'quit'
        return 'start_screen'

