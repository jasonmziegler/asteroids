import pygame
import constants
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
    
    # To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon(). It takes as inputs:
     # The screen object
    # A color (use "white")
    # A list of points (use the list returned by a call to the self.triangle() function)
    # in the Player class
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer > 0:
                pass
            else: 
                self.shot_cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        # Creates a new Shot at the current position of the player.
        shot = Shot(self.position.x,self.position.y,constants.SHOT_RADIUS)
        # Sets the shot's .velocity attribute:
        # Start with a pygame.Vector2 of (0, 1).
        shot.velocity = pygame.Vector2(0, 1)
        # .rotate() the vector in the direction the player is facing.
        rotated_shot = shot.velocity.rotate(self.rotation)
        # Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster.
        shot.velocity = rotated_shot * constants.PLAYER_SHOOT_SPEED
