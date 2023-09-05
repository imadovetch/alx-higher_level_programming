#!/usr/bin/python3
for ascii_value in range(ord('a'), ord('z') + 1):
    if chr(ascii_value) == 'e' or ascii_value == 'q':
        continue
    print(chr(ascii_value), end='')