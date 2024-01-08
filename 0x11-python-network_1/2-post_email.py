#!/usr/bin/python3
""" script that takes in a URL and an email,
sends a POST request to the passed URL"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("utf-8")
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
