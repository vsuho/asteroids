import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...] # Tuple with one or more sprite.Group objects

    def __init__(self, x: float, y: float, radius: float) -> None:
        # using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # Check for collision, returns True or False
    def collides_with(self, other):
        distance_between = self.position.distance_to(other.position)
        r1 = self.radius
        r2 = other.radius

        return distance_between <= r1 + r2


    
    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass