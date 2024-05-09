#!/usr/bin/python3
"""
Module for island perimeter function
"""


def island_perimeter(grid):
    """
    function that returns the perimeter of the island described in grid
    """
    if not grid:
        return 0

    perimeter = 0
    rows, columns = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
