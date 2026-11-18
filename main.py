import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

# Initialize pygame
pygame.init()

# GUI window, filled with black color
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def gameloop():
    while True:
        log_state()
        # Process the pygame event que
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the window with black
        screen.fill("black")
        # Refresh the screen
        pygame.display.flip()

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameloop()

if __name__ == "__main__":
    main()
    
