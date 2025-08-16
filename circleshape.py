import pygame

# Class for sprites (triangle is going to actually be a circle for easier collision)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # to be used later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes must override
        pass

    def update(self, dt):
        # Sub-classes must override
        pass