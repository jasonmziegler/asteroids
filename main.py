import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state
from logger import log_event


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    
    # Screen width: 1280
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    # Screen height: 720
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = constants.SCREEN_WIDTH/2 
    y = constants.SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x,y,constants.PLAYER_RADIUS)

    asteroidfield = AsteroidField()
    
    score = 0
    font = pygame.font.Font(None, 36)
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide_with(asteroid):
                    if asteroid.radius == 3:
                        score += 10
                    elif asteroid.radius == 2:
                        score += 20
                    else:
                        score += 40
                    log_event("asteroid_shot")
                    shot.kill()
                    # asteroid.kill()
                    asteroid.split()
            if player.collide_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for object in drawable:
            object.draw(screen)

        score_surface = font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (10,10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(dt)


if __name__ == "__main__":
    main()
