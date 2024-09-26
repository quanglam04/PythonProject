import pygame
from game import TankGame 
from StartScreen import StartScreen

def draw_text(text,font,text_col,x,y): 
    img = font.render(text,True,text_col)    
    pygame.display.set_mode((TankGame(1080, 720).window_width, TankGame(1080, 720).window_height)).blit(img,(x,y))
def main():
    pygame.init()
    game = TankGame(1024, 600)  
    window = pygame.display.set_mode((game.window_width, game.window_height ))
    pygame.display.set_caption("PROJECT GROUP 3 by Dat, Huy, Kien, Khoi, Lam")
    start_screen = StartScreen(game.window_width, game.window_height)

    while True:
        result = start_screen.handle_events(window)
        if result == 'start':
            game.run(window)
            break
        elif result == 'quit':
            break  
        start_screen.draw(window)
        pygame.display.flip()


if __name__ == "__main__": 
    main()
   