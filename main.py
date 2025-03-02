import pygame
from constants import *

def main():
    screen = init()
    draw(screen)

def init():
    pygame.init()
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def draw(screen):
    while True:
        if events():
            break
        pygame.Surface.fill(screen, BLACK)
        pygame.display.flip()

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


if __name__ == "__main__":
    main()