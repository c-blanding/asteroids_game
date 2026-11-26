import sys
import pygame
import constants as c
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        
        

        log_state()

        dt = clock.tick(60) / 1000
        print(f"dt: {dt}")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
            for shot in shots:
                if shot.check_collision(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
       

if __name__ == "__main__":
    main()
