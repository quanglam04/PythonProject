import heapq
import math

class Node:
    def __init__(self, x, y, g=math.inf, h=math.inf, f=math.inf):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def get_neighbors(node, grid):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = node.x + dx, node.y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '1':
            neighbors.append(Node(nx, ny))
    return neighbors

def a_star(start, end, grid):
    start.g = 0
    start.h = heuristic(start, end)
    start.f = start.h

    open_set = []
    heapq.heappush(open_set, start)
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)
        closed_set.add((current.x, current.y))

        if current.x == end.x and current.y == end.y:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        for neighbor in get_neighbors(current, grid):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            tentative_g = current.g + 1

            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None
