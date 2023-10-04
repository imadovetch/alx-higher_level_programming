#!/usr/bin/python3
"""Define naming-printing func"""


def say_my_name(first_name, last_name=""):
    """repre func
    Args:
        first_name: 1st name
        last_name: last_name
    return the full name otherwise error
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
