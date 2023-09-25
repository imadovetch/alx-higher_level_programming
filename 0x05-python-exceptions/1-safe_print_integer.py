#!/usr/bin/python3
def safe_print_integer(x):
    try:
        print("{:d}".format(x))
    except (TypeError, ValueError):
        return False
    return True
