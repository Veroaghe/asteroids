from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEED_MODIFIER
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color="white"):
        super().__init__(x, y, radius, color)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20.0, 50.0)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        colors = ["red", "blue", "green"]
        color_index = colors.index(self.color) - 1

        for i in range(2):
            if i == 1:
                angle *= -1
            
            new_vel = self.velocity.rotate(angle) * ASTEROID_SPEED_MODIFIER
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius, colors[color_index])
            new_asteroid.velocity = new_vel

        # v1 = self.velocity.rotate(angle) * 1.2
        # v2 = self.velocity.rotate(-angle) * 1.2

        # A1 = Asteroid(self.position.x, self.position.y, new_radius, colors[color_index])
        # A2 = Asteroid(self.position.x, self.position.y, new_radius, colors[color_index])

        # A1.velocity = v1
        # A2.velocity = v2