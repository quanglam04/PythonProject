import pygame
from game import TankGame
from StartScreen import StartScreen
import Setting
import LoadingBar
def main():
    flag = True
    pygame.init()
    window = pygame.display.set_mode((Setting.WIDTH, Setting.HEIGHT))
    pygame.display.set_caption(Setting.TITLE)
    start_screen = StartScreen(Setting.WIDTH, Setting.HEIGHT)
    while True:

        keyPress = LoadingBar.handle()

        if keyPress == 'Quit':
            flag = False
            break
        elif keyPress == 'Enter':
            break
    while True:
        if flag == False:
            break
        result = start_screen.handle_events(window)
        if result == 'start':
            game = TankGame(Setting.WIDTH, Setting.HEIGHT)
            game.run(window)
            break
        elif result == 'quit':
            break
        start_screen.draw(window)
        pygame.display.flip()


if __name__ == "__main__":
    main()
