import time
import pygame
import Setting
import button

check = False
result = {}


class StartScreen:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.keyControl = Setting.keyControl
        self.fire = Setting.fire

        self.font = pygame.font.SysFont(None, 55)
        self.background = pygame.image.load(Setting.background).convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Nút Start và Exit ban đầu
        self.start_btn = button.Button(395, 95, pygame.image.load(Setting.startBtn).convert_alpha(), 1)
        self.exit_btn = button.Button(395, 270, pygame.image.load(Setting.exitBtn).convert_alpha(), 1)

        # Các nút lựa chọn hiển thị sau khi nhấn Start
        self.option_1_btn = button.Button(63.4-10, 150, pygame.image.load(Setting.optionBtnOne).convert_alpha(), 0.7)
        self.option_2_btn = button.Button(303.55-10, 150, pygame.image.load(Setting.optionBtnTwo).convert_alpha(), 0.7)
        self.option_3_btn = button.Button(543.7-10, 150, pygame.image.load(Setting.optionBtnThree).convert_alpha(), 0.7)
        self.option_4_btn = button.Button(783.85-10,150,pygame.image.load(Setting.optionBtnFour).convert_alpha(),0.7)

        self.map_btns = []

        self.map_btns.append(button.Button(50 - 20, 50, pygame.image.load(Setting.map_1).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(250 - 20, 50, pygame.image.load(Setting.map_2).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(450 - 20, 50, pygame.image.load(Setting.map_3).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(650 - 20, 50, pygame.image.load(Setting.map_4).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(850 - 20, 50, pygame.image.load(Setting.map_5).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(50 - 20, 200, pygame.image.load(Setting.map_6).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(250 - 20, 200, pygame.image.load(Setting.map_7).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(450 - 20, 200, pygame.image.load(Setting.map_8).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(650 - 20, 200, pygame.image.load(Setting.map_9).convert_alpha(), 0.5))
        self.map_btns.append(button.Button(850 - 20, 200, pygame.image.load(Setting.map_10).convert_alpha(), 0.5))

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
            self.option_4_btn.draw(screen)
        else:
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
                    Setting.informationOfTank = 'asset/Stats/one-player.png'
                    self.show_maps = True  # Hiển thị các lựa chọn map
                elif self.option_2_btn.draw(screen):
                    result['numberOfPlayer'] = 2
                    Setting.informationOfTank = 'asset/Stats/two-player.png'
                    self.show_maps = True
                elif self.option_3_btn.draw(screen):
                    result['numberOfPlayer'] = 3
                    Setting.informationOfTank = 'asset/Stats/three-player.png'
                    self.show_maps = True
                elif self.option_4_btn.draw(screen):
                    result['numberOfPlayer'] = 4
                    Setting.informationOfTank = 'asset/Stats/four-player.png'
                    self.show_maps = True
            elif self.show_maps:
                for i, map_btn in enumerate(self.map_btns):
                    if map_btn.draw(screen):
                        result['selected_map'] = i + 1

                        # Hiển thị màn hình xám
                        screen.fill((128, 128, 128))  # Màu xám

                        # Đếm ngược từ 3, 2, 1, Start
                        font = pygame.font.Font(None, 150)

                        for countdown in range(3, 0, -1):
                            screen.fill((128, 128, 128))  # Làm mới màn hình xám
                            self.show(screen, result['numberOfPlayer'])
                            text = font.render(str(countdown), True, (255, 255, 255))  # Màu chữ trắng
                            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                                               screen.get_height() // 2 - text.get_height() // 2))
                            pygame.display.flip()  # Cập nhật màn hình
                            time.sleep(1)  # Dừng lại 1 giây

                        #     Hiển thị phím bấm các nút di chuyển


                        # Hiển thị 'Start'
                        screen.fill((128, 128, 128))
                        self.show(screen, result['numberOfPlayer'])
                        start_text = font.render('Start!', True, (255, 255, 255))
                        screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2,
                                                 screen.get_height() // 2 - start_text.get_height() // 2))
                        pygame.display.flip()
                        time.sleep(1)  # Hiển thị chữ 'Start' trong 1 giây


                        return 'start'

    def show(self, screen, numberOfPlayer):
        # Thiết lập font chữ và màu sắc
        font = pygame.font.SysFont(None, 40)
        color = (255, 255, 255)

        # Tạo danh sách các phím điều khiển cho từng người chơi
        controls = [
            {
                "up": Setting.up_player_1,
                "down": Setting.down_player_1,
                "left": Setting.left_player_1,
                "right": Setting.right_player_1,
                "hit": Setting.hit_player_1
            },
            {
                "up": Setting.up_player_2,
                "down": Setting.down_player_2,
                "left": Setting.left_player_2,
                "right": Setting.right_player_2,
                "hit": Setting.hit_player_2
            },
            {
                "up": Setting.up_player_3,
                "down": Setting.down_player_3,
                "left": Setting.left_player_3,
                "right": Setting.right_player_3,
                "hit": Setting.hit_player_3
            },
            {
                "up": Setting.up_player_4,
                "down": Setting.down_player_4,
                "left": Setting.left_player_4,
                "right": Setting.right_player_4,
                "hit": Setting.hit_player_4
            }
        ]

        # Lấy kích thước màn hình
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        # Xác định khoảng cách ngang giữa các cụm phím dựa trên số lượng người chơi
        positions = []
        for i in range(numberOfPlayer):
            x = (screen_width // (numberOfPlayer + 1)) * (i + 1)
            y = screen_height - 150  # khoảng cách từ cạnh dưới màn hình
            positions.append((x, y))

        # Vẽ các cụm phím điều khiển cho mỗi người chơi
        for i in range(numberOfPlayer):
            pos = positions[i]
            control = controls[i]

            # Tạo văn bản cho các phím điều khiển

            up_text = font.render(pygame.key.name(control["up"]), True, color)
            if pygame.key.name(control["up"]) == "up":
                up_text = pygame.font.SysFont(None, 30).render("UP", True, color)
            down_text = font.render(pygame.key.name(control["down"]), True, color)
            if pygame.key.name(control["down"]) == "down":
                down_text = pygame.font.SysFont(None, 30).render("DOWN", True, color)
            left_text = font.render(pygame.key.name(control["left"]), True, color)
            if pygame.key.name(control["left"]) == "left":
                left_text = pygame.font.SysFont(None, 30).render("LEFT", True, color)
            right_text = font.render(pygame.key.name(control["right"]), True, color)
            if pygame.key.name(control["right"]) == "right":
                right_text = pygame.font.SysFont(None, 30).render("RIGHT", True, color)
            hit_text = font.render(pygame.key.name(control["hit"]), True, color)
            if pygame.key.name(control["hit"]) == "hit":
                hit_text = pygame.font.SysFont(None, 30).render(pygame.key.name(control["hit"]), True, color)
            # Xác định vị trí các phím trong cụm bàn phím

            player_text = font.render(f"Player {i + 1}:", True, color)
            Text = font.render("HIT:",True,color)
            screen.blit(player_text, (pos[0] - player_text.get_width() // 2-6, pos[1] - 70))  # Hiển thị "Player {i}"

            screen.blit(up_text, (pos[0] - up_text.get_width() // 2, pos[1] - 30))  # Phím "up" phía trên
            if pygame.key.name(control["left"]) == "left":
                screen.blit(left_text, (pos[0] - 90, pos[1]))  # Phím "left" bên trái
            else:
                screen.blit(left_text, (pos[0] - 55, pos[1]))  # Phím "left" bên trái
            screen.blit(down_text, (pos[0] - down_text.get_width() // 2, pos[1]))  # Phím "down" ở giữa
            screen.blit(right_text, (pos[0] + 40, pos[1]))  # Phím "right" bên phải
            screen.blit(Text, (pos[0] - hit_text.get_width() // 2-60, pos[1] + 40))  # Phím "hit" ở dưới
            screen.blit(hit_text, (pos[0] - hit_text.get_width() // 2, pos[1] + 40))  # Phím "hit" ở dưới




