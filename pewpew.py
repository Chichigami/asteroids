import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = velocity
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        return pygame.draw.circle(surface = screen, color = "blue", center = self.position, radius = SHOT_RADIUS, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt