import pygame
import random
import time
import copy
from collections import deque

# Initializing variables needed for functions
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Futura', 50)
my_surface = my_font.render("Press 'r' to regenerate maze", False, (0, 0, 0))
# Change this to match your computer screen resolution
height = 1000
width = height * 3


def getColor(num):
    # 0 is wall
    if num == 0:
        return (0, 0, 0)
    # 1 is open space
    elif num == 1:
        return (242, 232, 207)
    # 2 is marker
    elif num == 2:
        return (56, 102, 65)
    # 3 is ending space
    elif num == 3:
        return (106, 153, 78)
    # 4 is path
    elif num == 4:
        return (167, 201, 87)
    # 5 is blocked
    elif num == 5:
        return (188, 71, 73)


def validCell(size, x, y):
    return 0 <= x < size and 0 <= y < size


def generateMaze(size):
    # Empty 2D Array
    myArray = [[0 for i in range(size)] for j in range(size)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    stack = [(0, 0)]
    myArray[0][0] = 1

    # Carving random DFS Paths
    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        found = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            wx, wy = x + dx // 2, y + dy // 2
            if validCell(size, nx, ny) and myArray[nx][ny] == 0:
                myArray[wx][wy] = 1
                myArray[nx][ny] = 1
                stack.append((nx, ny))
                found = True
                break
        # Backtracks if no valid neighboring cell
        if not found:
            stack.pop()
    # Start point
    myArray[0][0] = 2
    # Goal point
    myArray[size - 2][size - 2] = 3
    return myArray


def step(maze, stack):
    # Get current position
    marker = stack[len(stack) - 1]
    size = len(maze)
    x = marker[0]
    y = marker[1]
    # Stops at the solution path
    if x + y == 2 * size - 5:
        maze[x][y] = 4
        return False

    # Checks is cell above is valid and in path
    if validCell(size, x - 1, y) and maze[x - 1][y] == 1:
        maze[x][y] = 4
        maze[x - 1][y] = 2
        stack.append((x - 1, y))
        return True
    # Checks if cell below is valid and in path
    elif validCell(size, x + 1, y) and maze[x + 1][y] == 1:
        maze[x][y] = 4
        maze[x + 1][y] = 2
        stack.append((x + 1, y))
        return True
    # Checks if cell to left is valid and in path
    elif validCell(size, x, y - 1) and maze[x][y - 1] == 1:
        maze[x][y] = 4
        maze[x][y - 1] = 2
        stack.append((x, y - 1))
        return True
    # Checks if cell to right is valid and in path
    elif validCell(size, x, y + 1) and maze[x][y + 1] == 1:
        maze[x][y] = 4
        maze[x][y + 1] = 2
        stack.append((x, y + 1))
        return True
    # If no valid path, backtrack and mark the cells as visited
    else:
        maze[x][y] = 5
        stack.pop()
        return True


def bfs(maze, queue, visited):
    if maze[len(maze) - 3][len(maze) - 2] == 4 or maze[len(maze) - 2][len(maze) - 3] == 4:
        return False

    if not queue:
        return True
    r, c = queue.popleft()

    # If this cell is the goal, reconstruct the successful path
    if maze[r][c] == 3:
        while (r, c) != (-1, -1):
            # Mark path as green
            maze[r][c] = 4
            r, c = visited[(r, c)]
        queue.clear()
        return True

    # Mark the current cell as visited if not already special cells
    if maze[r][c] not in {2, 3}:
        maze[r][c] = 5

    # Explores all neighbors
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and
                maze[nr][nc] in {1, 3} and (nr, nc) not in visited):
            visited[(nr, nc)] = (r, c)
            queue.append((nr, nc))
            if maze[nr][nc] != 3:
                maze[nr][nc] = 5
    return True
