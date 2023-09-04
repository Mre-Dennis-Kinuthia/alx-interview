#!/usr/bin/python3
"""Lockboxes Interview Question"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be open with the keys available
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked initially

    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)  # Check if all boxes are visited


# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
