import pygame
from game import TankGame
from StartScreen import StartScreen
import Setting

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    pygame.display.set_mode((TankGame(1080, 720).window_width, TankGame(1080, 720).window_height)).blit(img,(x,y))
def main():
    pygame.init()
    window = pygame.display.set_mode((Setting.WIDTH, Setting.HEIGHT))
    pygame.display.set_caption(Setting.TITLE)
    start_screen = StartScreen(Setting.WIDTH, Setting.HEIGHT)

    while True:
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
