from circleshape import CircleShape
import pygame
from constants import *

# Child class of CircleShape
class Shot(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, radius=SHOT_RADIUS)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        