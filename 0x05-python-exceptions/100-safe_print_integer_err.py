#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: Unknown format code 'd' for object of type 'str'")
        return False
    return True
