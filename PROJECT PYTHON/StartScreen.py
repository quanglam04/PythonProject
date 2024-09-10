

import pygame
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

        self.map_btns = []

        self.map_btns.append(button.Button(50 - 20, 50, pygame.image.load(f"asset/map/map{1}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(250 - 20, 50, pygame.image.load(f"asset/map/map{2}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(450 - 20, 50, pygame.image.load(f"asset/map/map{3}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(650 - 20, 50, pygame.image.load(f"asset/map/map{4}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(850 - 20, 50, pygame.image.load(f"asset/map/map{5}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(50 - 20, 200, pygame.image.load(f"asset/map/map{6}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(250 - 20, 200, pygame.image.load(f"asset/map/map{7}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(450 - 20, 200, pygame.image.load(f"asset/map/map{8}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(650 - 20, 200, pygame.image.load(f"asset/map/map{9}.png").convert_alpha(), 0.5))
        self.map_btns.append(button.Button(850 - 20, 200, pygame.image.load(f"asset/map/map{10}.png").convert_alpha(), 0.5))

        self.show_options = False  # Kiểm soát việc hiển thị các lựa chọn
        self.show_maps = False  # Kiểm soát việc hiển thị các map

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        if self.show_maps:
            # Hiển thị các nút lựa chọn map
            for i, map_btn in enumerate(self.map_btns):
                row = i // 2  # Tính hàng của nút (mỗi hàng có 2 nút)
                col = i % 2   # Tính cột của nút
                map_btn.draw(screen)
        elif self.show_options:

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
            if not self.show_options and not self.show_maps:
                if self.start_btn.draw(screen):
                    self.show_options = True  # Hiển thị các lựa chọn người chơi
                elif self.exit_btn.draw(screen):
                    return 'quit'
            elif self.show_options and not self.show_maps:
                if self.option_1_btn.draw(screen):
                    result['numberOfPlayer'] = 1
                    self.show_maps = True  # Hiển thị các lựa chọn map
                elif self.option_2_btn.draw(screen):
                    result['numberOfPlayer'] = 2
                    self.show_maps = True
                elif self.option_3_btn.draw(screen):
                    result['numberOfPlayer'] = 3
                    self.show_maps = True
            elif self.show_maps:
                for i, map_btn in enumerate(self.map_btns):
                    if map_btn.draw(screen):
                        result['selected_map'] = i + 1
                        return 'start'

