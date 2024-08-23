import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        return pygame.draw.circle(surface = screen, color = "red", center = self.position, radius = self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt