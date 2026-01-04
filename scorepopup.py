import pygame
import constants

class ScorePopup(pygame.sprite.Sprite):
    def __init__(self, position, points, font):
        super().__init__()
        for group in self.containers:
            group.add(self)
        self.position = position
        self.time_to_live = constants.POPUP_TTL
        self.velocity = pygame.Vector2(0, -80)
        self.surface = font.render(f"+{points}", True, "yellow")
        self.rect = self.surface.get_rect(center=position)

    def update(self, dt):
        self.time_to_live -= dt
        self.position += self.velocity * dt
        self.rect.center = self.position
        if self.time_to_live < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.surface, self.rect)