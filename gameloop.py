import pygame
import sys
from logger import log_state, log_event
from initialize_game import * 

def gameloop():

    # Game initialization
    screen, clock, updatable, drawable, asteroids, shots, player = initialize_game()

    # Delta time
    dt = 0.0

    # Loop until the game ends
    while True:
        log_state()
        # Process the pygame event que

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update updatable objects each frame
        updatable.update(dt)

        # Go through every asteroid in asteroids and check for collision
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
            # Use the same asteroid for checking if each one is shot
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_hit")
                    asteroid.kill()
                    shot.kill()

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