import pygame
from game import TankGame

game = TankGame(980, 620)
window = pygame.display.set_mode((game.window_width, game.window_height))
pygame.display.set_caption("PROJECT GROUP 3 by Dat, Huy, Kien, Khoi, Lam")
game.run(window)
