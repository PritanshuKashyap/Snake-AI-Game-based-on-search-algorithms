import heapq  
from grid import get_neighbors
   
def heuristic(a, b):  
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal, snake_body):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for neighbor in get_neighbors(current, snake_body):

            if neighbor in snake_body:
                continue

            temp_g = g_score[current] + 1

            if neighbor not in g_score or temp_g < g_score[neighbor]:

                g_score[neighbor] = temp_g
                f = temp_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f, neighbor))
                came_from[neighbor] = current

    path = []
    node = goal

    if node not in came_from:
        return []

    while node != start:
        path.append(node)
        node = came_from[node]

    path.reverse()
    return path
