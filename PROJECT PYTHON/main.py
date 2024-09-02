import sys
import pygame
from bullet import Bullet
from game import TankGame


game = TankGame(1080, 630)
window = pygame.display.set_mode((game.window_width, game.window_height))
pygame.display.set_caption("PROJECT GROUP 3 by Dat, Huy, Kien, Khoi, Lam")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet object and add it to the game
                bullet = Bullet(game)  # Assuming you have a Bullet class
                game.bullets.append(bullet)
                print("Nút space được nhấn")

    game.run(window)