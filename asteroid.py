from circleshape import CircleShape
import pygame
from constants import *
import random

# Child class of CircleShape
class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(random_angle)
            vect2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            spawn1, spawn2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
            spawn1.velocity, spawn2.velocity = vect1 * 1.2, vect2 * 1.2