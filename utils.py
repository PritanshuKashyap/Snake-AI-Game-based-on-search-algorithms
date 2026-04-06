import pygame
from settings import *

def draw_grid(screen):

    for x in range(ROWS):
        for y in range(COLS):

            rect = pygame.Rect(
                y * CELL_SIZE,
                x * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, WHITE, rect, 1)