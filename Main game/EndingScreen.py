import pygame
import Setting
import button

class EndingScreen:
    def __init__(self, winner_id, width, height):
        self.winner_id = winner_id
        self.width = width
        self.height = height

        self.font = pygame.font.SysFont(None, 75)
        self.background = pygame.image.load(Setting.background).convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.quit_btn = button.Button(100, 390, pygame.image.load(Setting.exitBtn).convert_alpha(), 1)
        self.replay_btn = button.Button(630, 390, pygame.image.load(Setting.startBtn).convert_alpha(), 1)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        # Display winner text
        winner_text = self.font.render(f"Player {self.winner_id + 1} Wins!", True, (255, 255, 255))
        screen.blit(winner_text, (self.width // 2 - winner_text.get_width() // 2, self.height // 3))

        # Draw buttons
        self.quit_btn.draw(screen)
        self.replay_btn.draw(screen)

    def handle_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if self.quit_btn.draw(screen):
                return 'quit'
            elif self.replay_btn.draw(screen):
                return 'replay'
