from settings import *

def get_neighbors(pos, snake_body):
    x, y = pos

    neighbors = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]

    valid = []

    for n in neighbors:
        nx, ny = n

        # inside grid
        if 0 <= nx < (WIDTH // CELL_SIZE) and 0 <= ny < (HEIGHT // CELL_SIZE):
            # avoid snake body
            if n not in snake_body:
                valid.append(n)

    return valid