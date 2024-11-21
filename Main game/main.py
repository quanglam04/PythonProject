import pygame
from pygame import FULLSCREEN

from game import TankGame
from StartScreen import StartScreen
import Setting
import LoadingBar
from EndingScreen import EndingScreen
def main():
    flag = True
    pygame.init()
    print(Setting.Window_mode)

    if Setting.Window_mode :
        window = pygame.display.set_mode((Setting.WIDTH,Setting.HEIGHT))
    else:
        window = pygame.display.set_mode((Setting.WIDTH, Setting.HEIGHT),FULLSCREEN)
    pygame.display.set_caption(Setting.TITLE)

    #Chay LoadingBar 1 lan
    while True:
        keyPress = LoadingBar.handle()

        if keyPress == 'Quit':
            flag = False
            break
        elif keyPress == 'Enter':
            break

    # Hiển thị màn hình bắt đầu (cho phép chọn chế độ chơi và bản đồ)
    start_screen = StartScreen(Setting.WIDTH, Setting.HEIGHT)

    #Vong lap cua game
    while True:

        while True:
            if flag == False:
                break
            result = start_screen.handle_events(window)
            if result == 'start':
                break
            elif result == 'quit':
                return
            start_screen.draw(window)
            pygame.display.flip()

        #Chay game
        game = TankGame(Setting.WIDTH, Setting.HEIGHT)
        winner_id = game.run(window)

        # Hiển thị màn hình kết thúc nếu có người chiến thắng
        if winner_id is not None:
            ending_screen = EndingScreen(winner_id, Setting.WIDTH, Setting.HEIGHT)
            while True:
                ending_screen.draw(window)
                event_result = ending_screen.handle_events(window)
                if event_result == 'quit':
                    return  # Thoát game
                elif event_result == 'replay':
                    break  # Quay lại StartScreen
                pygame.display.flip()


if __name__ == "__main__":
    main()
