import pygame
import random
from src.core.constants import ASTEROID_MIN_RADIUS
from src.core.circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        return pygame.draw.circle(surface = screen, color = "red", center = self.position, radius = self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if not self.radius <= ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            vel_1 = self.velocity.rotate(random_angle)
            vel_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius).velocity = vel_1 * 1.2
            Asteroid(self.position.x, self.position.y, new_radius).velocity = vel_2 * 1.2