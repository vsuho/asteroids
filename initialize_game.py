import pygame
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from create_groups import create_groups
from player import Player

def initialize_game():
    # Initialize pygame
    pygame.init()

    # GUI window, filled with black color
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updatable, drawable, asteroids = create_groups()

    # AsteroidField instance
    af = AsteroidField()

    # Player initialization
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    return screen, clock, updatable, drawable, asteroids, player
    
