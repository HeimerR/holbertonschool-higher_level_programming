#!/usr/bin/python3
""" takes in a URL, and displays the value of the X-Request-Id """
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        r = urllib.request.urlopen(argv[1])
        print(r.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
