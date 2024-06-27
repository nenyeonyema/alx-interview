#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ returns the perimeter of the island
    described in grid(a list of list of integers).
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check top neighbor
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check left neighbor
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right neighbor
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
