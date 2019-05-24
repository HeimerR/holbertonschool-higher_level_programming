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
"""    while i < (len(text) - 1):
        print("preletter:{}".format(i))
        print("{}".format(text[i]), end='')
        if text[i] is "." or text[i] is "?" or text[i] is ":":
            print("\n")
            print("interno{}".format(i))
            while (text[i + 1] is " " and (i < len(text) - 1)):
                i += 1
               print("interno2{}]".format(i))
        i += 1
    if  text[i] is "." or text[i] is "?" or text[i] is ":":
        print("\n")
    if text[i] is not " ":
        print(text[i], end='')
"""
    text.replace(".", "\n\n")
    text.replace("?", "\n\n")
    text.replace(":", "\n\n")
    print(text)
