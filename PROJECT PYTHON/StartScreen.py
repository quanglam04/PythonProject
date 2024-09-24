import pygame
import sys
import button

result = {}
class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 55)
        self.background = pygame.image.load("asset/background.jpg").convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Nút Start và Exit ban đầu
        self.start_btn = button.Button(395, 95, pygame.image.load("asset/start_btn_newVersion.png").convert_alpha(), 1)
        self.exit_btn = button.Button(395, 270, pygame.image.load("asset/save_btn_newVersion.png").convert_alpha(), 1)

        # Các nút lựa chọn hiển thị sau khi nhấn Start
        self.option_1_btn = button.Button(60, 150, pygame.image.load("asset/1_player_btn.png").convert_alpha(), 1)
        self.option_2_btn = button.Button(372.5, 150, pygame.image.load("asset/2_player_btn.png").convert_alpha(), 1)
        self.option_3_btn = button.Button(685, 150, pygame.image.load("asset/3_player_btn.png").convert_alpha(), 1)

        self.show_options = False  # Kiểm soát việc hiển thị các tùy chọn

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        if self.show_options:
            # Hiển thị các nút lựa chọn
            self.option_1_btn.draw(screen)
            self.option_2_btn.draw(screen)
            self.option_3_btn.draw(screen)
        else:
            # Hiển thị nút Start và Exit ban đầu
            self.start_btn.draw(screen)
            self.exit_btn.draw(screen)

    def handle_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if not self.show_options:
                if self.start_btn.draw(screen):
                    self.show_options = True  # Ẩn nút Start và Exit, hiện các lựa chọn
                elif self.exit_btn.draw(screen):
                    return 'quit'
            else:
                # Xử lý sự kiện khi các tùy chọn hiển thị
                if self.option_1_btn.draw(screen):
                    result['numberOfPlayer'] = 1
                    return 'start'
                elif self.option_2_btn.draw(screen):
                    result['numberOfPlayer'] = 2
                    return 'start'
                elif self.option_3_btn.draw(screen):
                    result['numberOfPlayer'] = 3
                    return 'start'
        return 'start_screen'