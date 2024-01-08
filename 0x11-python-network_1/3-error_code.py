#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8) """
from urllib import error, request
import sys


if __name__ == "__main__":

    req = request.Request(sys.argv[1])

    try:
        with request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
