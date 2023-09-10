#!/usr/bin/python3
"""
Island Perimeter Interview Question
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += 4
                # Left
                if (((row - 1) >= 0) and (grid[row - 1][col] == 1)):
                    perimeter -= 1
                    # Right
                if (((row + 1) < len(grid)) and (grid[row + 1][col] == 1)):
                    perimeter -= 1
                    # Top
                if (((col - 1) >= 0) and (grid[row][col - 1] == 1)):
                    perimeter -= 1
                    # Bottom
                if (((col + 1) < len(grid[0])) and (grid[row][col + 1] == 1)):
                    perimeter -= 1
    return perimeter
