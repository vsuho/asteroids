import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from gameloop import gameloop

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameloop()
    

if __name__ == "__main__":
    main()
    
