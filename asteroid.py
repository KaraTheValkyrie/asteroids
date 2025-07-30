# import stuff
from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_rotation = random.uniform(20, 50)
        vector_one = (self.velocity.copy()).rotate(random_rotation)
        vector_two = (self.velocity.copy()).rotate(random_rotation * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(0, 0, new_radius)
        asteroid_one.position = self.position.copy()
        asteroid_one.velocity = vector_one.copy() * 1.2
        asteroid_two = Asteroid(0, 0, new_radius)
        asteroid_two.position = self.position.copy()
        asteroid_two.velocity = vector_two.copy() * 1.2