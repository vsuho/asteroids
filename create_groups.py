import pygame
from classes.player import Player
from classes.asteroid import Asteroid
from classes.asteroidfield import AsteroidField
from classes.shot import Shot

def create_groups():

    # Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add Player class to the groups
    Player.containers = (updatable, drawable)

    # Add Asteroid class to the groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add AsteroidField class to updatable group, as it's not drawable or asteroid
    AsteroidField.containers = updatable

    # Add Shot class to shots, drawable, updatable groups
    Shot.containers = (shots, drawable, updatable)

    return updatable, drawable, asteroids, shots