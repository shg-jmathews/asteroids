import pygame
from circleshape import *
from constants import *
import random

# Base class for game objects
class Asteroid(CircleShape):
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

    def split(self):
        self.kill()
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vec1 = pygame.Vector2.rotate(self.velocity, angle)
            vec2 = pygame.Vector2.rotate(self.velocity, -angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position[0], self.position[1], new_radius)
            a2 = Asteroid(self.position[0], self.position[1], new_radius)
            a1.velocity = vec1 * 1.2
            a2.velocity = vec2 * 1.2