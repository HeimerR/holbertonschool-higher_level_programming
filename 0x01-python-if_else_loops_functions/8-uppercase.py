#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        a = str[i]
        aux = chr(ord(a) - 32) if (ord(a) > 96 and ord(a) < 123) else a
        print('{}'.format(aux), end='')
    print()
