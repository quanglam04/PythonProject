import pygame
from Tank import TankGame

if __name__ == "__main__":
    #pygame.init()  according to the wiki, pygame.Joystick.init is deprecated (it should have been removed since pygame 2.1, but it seems it didn't get removed
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tank")

    game = TankGame(WINDOW_WIDTH, WINDOW_HEIGHT)
    game.run(window)