#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        info = {"q": argv[1]}
    else:
        info = {"q": ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] ".format(r.json().get("id")), end="")
            print(r.json().get("name"))
    except:
        print("Not a valid JSON")
