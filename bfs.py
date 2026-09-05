from collections import deque
from grid import get_neighbors 
 
def bfs(start, goal, snake_body):
    queue = deque([start])
    visited = {start: None}
  
    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for neighbor in get_neighbors(current, snake_body):
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = current

    path = []
    cur = goal

    while cur != start and cur in visited:
        path.append(cur)
        cur = visited[cur]

    path.reverse()
    return path
