import pygame
import constants
from circleshape import CircleShape
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            asteroid_one_vector = self.velocity.rotate(angle)
            asteroid_two_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = asteroid_one_vector * 1.2
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two.velocity = asteroid_two_vector * 1.2

