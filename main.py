import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random, sys


def main():
    print("Starting Asteroids!")
    pygame.init()
    pygame.font.init()
    score_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player, dt, score, updatable, drawable, asteroids, shots = setup()
    # dt = 0
    # score = 0

    # updatable = pygame.sprite.Group()
    # drawable = pygame.sprite.Group()
    # asteroids = pygame.sprite.Group()
    # shots = pygame.sprite.Group()

    # Player.containers = (updatable, drawable)
    # Asteroid.containers = (asteroids, updatable, drawable)
    # AsteroidField.containers = (updatable)
    # Shot.containers = (shots, updatable, drawable)
    

    # player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # AsteroidField()

    # add_shadow_elite(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)

        updatable.update(dt)

        # Checking collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                print(f"Final Score: {score}")
                # sys.exit()
                player, dt, score, updatable, drawable, asteroids, shots = setup()
            
            for shot in shots:
                r = shot.radius
                if not (0 - r < shot.position.x < SCREEN_WIDTH + r) or not (0 - r < shot.position.y < SCREEN_HEIGHT + r):
                    shot.kill()
                if asteroid.collision(shot):
                    score += asteroid.points
                    asteroid.split()
                    shot.kill()
        
        for obj in drawable:
            obj.draw(screen)

        score_text = score_font.render(f"Score: {score}", False, "white")
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def setup():
    dt = 0
    score = 0

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

    return player, dt, score, updatable, drawable, asteroids, shots


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