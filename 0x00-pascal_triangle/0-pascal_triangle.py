#!/usr/bin/python3
"""
Pascal's Triangle Implementation
"""


def pascal_triangle(n):
    """Returns the factorial of an integer"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[i - 1]
            row = [1]  # The first element of each row is always 1
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle


# Test cases
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
