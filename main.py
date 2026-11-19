import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def gameloop():

    # Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add Player class to the groups
    Player.containers = (updatable, drawable)

    # Add Asteroid class to the groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add AsteroidField class to updatable group, as it's not drawable or asteroid
    AsteroidField.containers = (updatable)

    af = AsteroidField()

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

        # Update updatable objects each frame
        updatable.update(dt)

        # Fill the window with black
        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        # Refresh the screen
        pygame.display.flip()
        
        # tick method returns how many ms have passed since last call
        # divide it by 1000, so it returns as seconds
        # FPS capped at 60
        dt = clock.tick(60) / 1000
        


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameloop()
    

if __name__ == "__main__":
    main()
    
