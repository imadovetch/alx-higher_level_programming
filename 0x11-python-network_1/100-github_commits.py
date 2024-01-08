#!/usr/bin/python3
""" evaluates candidates applying for a back-end
position with multiple technical challenges """
import sys
import requests


if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".\
        format(sys.argv[2], sys.argv[1])
    content = requests.get(url).json()

    try:
        for r in range(10):
            print("{}: {}".format(
                content[r].get("sha"),
                content[r].get("commit").get("author").get("name")))
    except IndexError:
        pass
