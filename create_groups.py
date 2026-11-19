import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def create_groups():
    
    # Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add Player class to the groups
    Player.containers = (updatable, drawable)

    # Add Asteroid class to the groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add AsteroidField class to updatable group, as it's not drawable or asteroid
    AsteroidField.containers = updatable

    return updatable, drawable, asteroids