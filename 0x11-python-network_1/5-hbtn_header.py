#!/usr/bin/python3
"""  fetches X-Request-Id """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.head(argv[1])
    print(r.headers.get('X-Request-Id'))
