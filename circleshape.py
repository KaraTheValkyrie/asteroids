from constants import *
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        #other must be another CircleShape object
        #or something that inherits from CircleShape
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        return distance < self.radius + other.radius
    
    def screenwrap(self):
        #check left edge
        if self.position.x < (self.radius * -1):
            self.position.update(SCREEN_WIDTH + self.radius, self.position.y)
        
        #check right edge
        if self.position.x > (self.radius + SCREEN_WIDTH):
            self.position.update(self.radius * -1, self.position.y)
        
        #check bottom edge
        if self.position.y > (self.radius + SCREEN_HEIGHT):
            self.position.update(self.position.x, self.radius * -1)

        #check top edge
        if self.position.y < (self.radius * -1):
            self.position.update(self.position.x, self.radius + SCREEN_HEIGHT)