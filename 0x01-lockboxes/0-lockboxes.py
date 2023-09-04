#!/usr/bin/python3
"""Lockboxes Interview Question"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be open with the keys available
    """
    given_keys = boxes[0]
    all_keys = []
    for count, key in enumerate(given_keys, 1):
        all_keys = given_keys.copy()
        if key < len(boxes) and not boxes[key]:
            all_keys.append(0)
        else:
            all_keys.extend(boxes[key])

        # Removing duplicate keys
        for i in all_keys:
            if i not in given_keys and i < len(boxes):
                given_keys.append(i)
            if 0 not in given_keys:
                given_keys.append(0)

        if (count == len(boxes)):
            return True

    return False
