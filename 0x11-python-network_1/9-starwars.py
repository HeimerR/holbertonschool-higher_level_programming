#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import requests
from sys import argv

if __name__ == "__main__":
    search = {'search': argv[1]}
    r = requests.get("https://swapi.co/api/people/", params=search)
    result_num = r.json().get('count')
    print("Number of results: {}".format(result_num))
    result_list = r.json().get('results')
    for res in range(0, len(result_list)):
        print(result_list[res].get('name'))
