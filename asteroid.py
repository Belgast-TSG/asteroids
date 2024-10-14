from circleshape import *
from constants import *
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = pygame.Color('white')
        position = self.position
        radius = self.radius
        width = 2
        pygame.draw.circle(screen, color, position, radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)