#import the circle shape, which this is a child of
from circleshape import *

#define a constant for the shot size
SHOT_RADIUS = 5

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(0, 0, SHOT_RADIUS)
        self.position = position
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt