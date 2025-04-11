import pygame
from circleshape import *
from constants import *

# Base class for game objects
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pass

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt
        pass