#!/usr/bin/python3
""" module that prins new lines after some characters
"""


def text_indentation(text):
    """function that prints a text with 2 new lines
       after each of these characters: ., ? and :
    Args:
        text (str): string to print
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    aux = text.replace(".", ".\n\n")
    aux2 = aux.replace("?", "?\n\n")
    aux = aux2.replace(":", ":\n\n")
    aux2 = aux.rstrip(" ")
    aux = aux2.lstrip(" ")
    aux3 = aux.split("\n")
    for i in range(len(aux3)):
        aux3[i] = aux3[i].rstrip(" ")
        aux3[i] = aux3[i].lstrip(" ")
    print('\n'.join(aux3), end='')
