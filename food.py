import random
from settings import *

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1)
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1)
        return (x, y)

    def respawn(self, snake_body):
        while True:
            pos = self.random_position()
            if pos not in snake_body:
                self.position = pos
                break

    def draw(self, screen):
        import pygame
        rect = pygame.Rect(
            self.position[0] * CELL_SIZE,
            self.position[1] * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(screen, RED, rect)