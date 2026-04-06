import pygame
from settings import *
from snake import Snake
from food import Food
from utils import draw_grid

from bfs import bfs
from Dfs import dfs
from astar import astar

BLUE = (0, 0, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT+50))
pygame.display.set_caption("Snake AI - BFS / DFS / A*")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

snake = Snake()
food = Food()
score = 0

font = pygame.font.SysFont("Arial", 30)

algorithm = "bfs"   # default

# Button rectangles
bfs_btn = pygame.Rect(10, HEIGHT+10, 80, 30)
dfs_btn = pygame.Rect(110, HEIGHT+10, 80, 30)
astar_btn = pygame.Rect(210, HEIGHT+10, 80, 30)




font = pygame.font.SysFont("Arial", 30)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            if bfs_btn.collidepoint(mouse):
                algorithm = "bfs"

            if dfs_btn.collidepoint(mouse):
                algorithm = "dfs"

            if astar_btn.collidepoint(mouse):
                algorithm = "astar"

    start = snake.get_head()
    goal = food.position

    # Select algorithm
    if algorithm == "bfs":
        path = bfs(start, goal, snake.body)

    elif algorithm == "dfs":
        path = dfs(start, goal, snake.body)

    else:
        path = astar(start, goal, snake.body)

    if path:
        snake.move(path[0])

    # Eat food
    if snake.get_head() == food.position:
     snake.grow()
    score += 1
    food.respawn(snake.body)

    screen.fill(BLACK)

    draw_grid(screen)

    # Draw snake
    for block in snake.body:
        rect = pygame.Rect(
            block[1]*CELL_SIZE,
            block[0]*CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(screen, GREEN, rect)

    # Draw food
    rect = pygame.Rect(
        food.position[1]*CELL_SIZE,
        food.position[0]*CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )
    pygame.draw.rect(screen, RED, rect)

    # -------- DRAW BUTTONS --------

    pygame.draw.rect(screen, BLUE, bfs_btn)
    pygame.draw.rect(screen, BLUE, dfs_btn)
    pygame.draw.rect(screen, BLUE, astar_btn)

    screen.blit(font.render("BFS", True, WHITE), (25, HEIGHT+15))
    screen.blit(font.render("DFS", True, WHITE), (125, HEIGHT+15))
    screen.blit(font.render("A*", True, WHITE), (235, HEIGHT+15))

    # show current algorithm
    text = font.render(f"Algorithm: {algorithm.upper()}", True, WHITE)
    screen.blit(text, (350, HEIGHT+15))

    pygame.display.update()

pygame.quit()