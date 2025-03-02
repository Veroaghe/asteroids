import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random, sys


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # add_shadow_elite(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                r = shot.radius
                if not (0 - r < shot.position.x < SCREEN_WIDTH + r) or not (0 - r < shot.position.y < SCREEN_HEIGHT + r):
                    shot.kill()
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def add_shadow_elite(player):
    for _ in range(10):
        color = (
            random.randrange(0, 256),
            random.randrange(0, 256),
            random.randrange(0, 256),
        )

        offset = 100
        minX = player.position.x - offset
        maxX = player.position.x + offset
        minY = player.position.y - offset
        maxY = player.position.y + offset
        Player(random.randrange(minX, maxX), random.randrange(minY, maxY), color)


if __name__ == "__main__":
    main()