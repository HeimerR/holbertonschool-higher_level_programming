#!/usr/bin/python3
""" Star Wars fetch info  """
import requests
from sys import argv

if __name__ == "__main__":
    search = {'search': argv[1], 'page': '1'}

    def starwars(search):
        r = requests.get("https://swapi.co/api/people/", params=search)
        if search['page'] == '1':
            result_num = r.json().get('count')
            print("Number of results: {}".format(result_num))
        result_list = r.json().get('results')
        for res in range(0, len(result_list)):
            print(result_list[res].get('name'))
        return r.json().get('next')
    next = starwars(search)
    while next is not None:
        search['page'] = str(int(search['page']) + 1)
        next = starwars(search)
