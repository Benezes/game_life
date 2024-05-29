import sys
import time
from random import random
from typing import List

import pygame


def create_matrix_list_filled_with_zeros(width: int, height: int) -> List[List[int]]:
    return [[0 for _ in range(height)] for _ in range(width)]


def initiate_live_cells(
    grid: List[List[int]], probability: float = 0.3
) -> List[List[int]]:
    """
    Probability-Based Initialization:
    You can pass a probability value (e.g., 0.3 for 30%) to determine whether each cell should be alive.
    This approach ensures a more controlled and uniform distribution of live cells.
    """
    for l in range(len(grid)):
        for c in range(len(grid[0])):
            if random() < probability:
                grid[l][c] = 1
    return grid


def initialize_grid(
    width: int, height: int, probability: float = 0.3
) -> List[List[int]]:
    """
    Create a 2D list filled with 0s
    Set initial live cells based on some pattern
    """
    grid: List[List[int]] = create_matrix_list_filled_with_zeros(width, height)
    grid = initiate_live_cells(grid, probability)
    return grid


def create_window(grid: List[List[int]], width: int, height: int) -> None:
    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (50, 50, 50)

    CELL_SIZE = 20
    GRID_WIDTH = width
    GRID_HEIGHT = height
    SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
    SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game of Life")

    def draw_grid(screen, grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                color = WHITE if grid[row][col] == 1 else BLACK
                pygame.draw.rect(
                    screen,
                    color,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )
                pygame.draw.rect(
                    screen,
                    GRAY,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    1,
                )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.flip()

        grid = update_grid(grid)
        time.sleep(0.1)


def update_grid(grid: List[List[int]]) -> List[List[int]]:
    """
    Create a new grid of the same size
    For each cell (x, y) in the grid:
        Count the live neighbors
        Apply the Game of Life rules
        Set the cell in the new grid to alive or dead
    Return the new grid
    """
    w, h = len(grid), len(grid[0])
    new_grid = create_matrix_list_filled_with_zeros(w, h)

    for x in range(w):
        for y in range(h):
            live_neighbors = count_neighbors(grid, x, y)
            new_grid[x][y] = apply_rules(grid[x][y], live_neighbors)

    return new_grid


def apply_rules(current_state: int, live_neighbors: int) -> int:
    """
    Any live cell with fewer than two live neighbors dies (underpopulation).
    Any live cell with two or three live neighbors lives on to the next generation (survival).
    Any live cell with more than three live neighbors dies (overcrowding).
    Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
    """
    if current_state == 1 and live_neighbors < 2:
        return 0  # underpopulation
    if current_state == 1 and (live_neighbors == 2 or live_neighbors == 3):
        return 1  # survival
    if current_state == 1 and live_neighbors > 3:
        return 0  # overcrowding
    if current_state == 0 and live_neighbors == 3:
        return 1  # reproduction
    return current_state  # stays the same


def count_neighbors(grid: List[List[int]], x: int, y: int) -> int:
    """
    Initialize a count to 0
    Loop over the 8 neighbors
        If the neighbor is within bounds and alive, increment the count
    Return the count
    """
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if (i != x or j != y) and grid[i][j] == 1:
                    count += 1
    return count


def main():
    width = 45
    height = 45

    grid = initialize_grid(width=width, height=height, probability=0.3)
    create_window(grid, width, height)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
