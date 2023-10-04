#!/usr/bin/python3
"""define a func that orint the square number"""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
