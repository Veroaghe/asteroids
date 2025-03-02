import pygame
from constants import *
from player import Player
import random

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # add_shadow_elite()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)
        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def add_shadow_elite():
    for _ in range(200):
        color = (
            random.randrange(0, 256),
            random.randrange(0, 256),
            random.randrange(0, 256),
        )
        Player(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT), color)


if __name__ == "__main__":
    main()