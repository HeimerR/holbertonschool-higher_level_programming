#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import requests
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)
