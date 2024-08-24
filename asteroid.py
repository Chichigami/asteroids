import pygame
import random
from constants import ASTEROID_MIN_RADIUS
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
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vel_1 = self.velocity.rotate(random_angle)
        vel_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_split_1.velocity = vel_1
        asteroid_split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_split_2.velocity = vel_2