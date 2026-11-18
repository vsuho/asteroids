import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def gameloop():

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Initialize pygame
    pygame.init()

    # GUI window, filled with black color
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    # Delta time
    dt = 0.0

    while True:
        log_state()
        # Process the pygame event que

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the window with black
        screen.fill("black")

        player.draw(screen)
        
        # Refresh the screen
        pygame.display.flip()
        
        # tick method returns how many ms have passed since last call
        # divide it by 1000, so it returns as seconds
        # FPS capped at 60
        dt = clock.tick(60) / 1000
        #print(dt)


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameloop()
    

if __name__ == "__main__":
    main()
    
