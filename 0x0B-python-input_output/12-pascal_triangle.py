#!/usr/bin/python3
"""
Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for t in range(n - 1):
        line = [1]
        for i in range(t):
            line.append(triangle[t][i] + triangle[t][i + 1])

        line.append(1)
        triangle.append(line)

    return triangle
