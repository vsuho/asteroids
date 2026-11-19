import pygame
import random
from classes.circleshape import CircleShape
from constants import * 
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.center = x / 2 * y / 2
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    # Method that splits asteroid when shot (if asteroid is big enough),
    # kill the original and spawn two smaller ones
    def split(self) -> None:
        self.kill()

        # If asteroid is small, return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Otherwise, spawn 2 smaller asteroids
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position

        # Create new Asteroid instances at self.position (x, y) with new smaller radius
        asteroid_1 = Asteroid(x, y, new_radius)
        asteroid_2 = Asteroid(x, y, new_radius)

        asteroid_1.velocity = new_vector1 * 1.2
        asteroid_2.velocity = new_vector2 * 1.2
        







