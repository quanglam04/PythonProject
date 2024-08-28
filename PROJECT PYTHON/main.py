import pygame
from game import TankGame

game = TankGame(1080, 720)
window = pygame.display.set_mode((game.window_width, game.window_height))
pygame.display.set_caption("PROJECT GROUP 3 by Dat, Huy, Kien, Khoi, Lam")
game.run(window)

