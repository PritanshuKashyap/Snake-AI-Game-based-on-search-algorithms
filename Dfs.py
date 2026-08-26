from grid import get_neighbors
  
def dfs(start, goal, snake_body):
   
    stack = [start]
    visited = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        for neighbor in get_neighbors(current, snake_body):

            if neighbor in snake_body:
                continue

            if neighbor not in visited:
                stack.append(neighbor)
                visited[neighbor] = current

    path = []
    node = goal

    if node not in visited:
        return []

    while node != start:
        path.append(node)
        node = visited[node]

    path.reverse()
    return path
