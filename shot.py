from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt