#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Doc
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    
    # If last element => find another integer
    if list[-1] == result:
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] != list[-1]:
                result = list[i]
                break
            i += 1
    
    return result
