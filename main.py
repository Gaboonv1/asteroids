import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)
        for collision in asteroids:
             if player.collides_with(collision) == True:
                  log_event("player_hit")
                  print("Game over!")
                  sys.exit()
        for pieces in asteroids:
             for hit in shots:
                  if pieces.collides_with(hit) == True:
                       log_event("asteroid_shot")
                       pieces.split()
                       hit.kill()

        screen.fill("black")
        for d in drawable:
                d.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


