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
            try:
                print(result_list[res].get('name'))
            except UnicodeEncodeError:
                print(result_list[res].get('name').encode("utf-8"))
            for film in result_list[res].get('films'):
                r2 = requests.get(film)
                title = r2.json().get('title')
                print("\t{}".format(title))
        return r.json().get('next')
    next = starwars(search)
    while next is not None:
        search['page'] = str(int(search['page']) + 1)
        next = starwars(search)
