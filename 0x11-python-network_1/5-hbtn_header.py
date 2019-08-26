#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.head(argv[1])
    print(r.headers.get('X-Request-Id'))
