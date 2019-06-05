#!/usr/bin/python3
"""module 
reads n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8)
        and prints it to stdout
    """
    with open(filename, encoding='utf-8') as my_file:
        if nb_lines <= 0 or nb_lines >= len(my_file.readlines()):
            my_file.seek(0)
            print(my_file.read(), end="")
        else:
            my_file.seek(0)
            for i in range(nb_lines):
                print(my_file.readline(), end="")                    
