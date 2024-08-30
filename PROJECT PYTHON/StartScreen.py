import pygame
import sys

class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 55)

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Màu nền đen
        title_text = self.font.render("Press 'S' to Start or 'Q' to Quit", True, (255, 255, 255))
        text_rect = title_text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(title_text, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return 'start'
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        return 'start_screen'
