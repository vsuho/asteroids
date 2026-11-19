import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0

    # Method to draw the triangle
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # Method to rotate player's triangle
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to move player's triangle
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # Control sprite behaviour
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # a is pressed, rotate counter-clockwise
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # d is pressed, rotate clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)

        # w is pressed, move forward
        if keys[pygame.K_w]:
            self.move(dt)

        # s is pressed, move backwards
        if keys[pygame.K_s]:
            self.move(-dt)

    # Calculate and return three points of player ship,
    # this is then passed to the draw method
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
