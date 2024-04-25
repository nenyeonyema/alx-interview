#!/usr/bin/python3
"""
0-Paschal-Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # first element of each row is always 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])  # middle elements
        new_row.append(1)  # last element of each row is always 1
        triangle.append(new_row)

    return triangle
