#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    symbols = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    roman_list = list(roman_string)
    num = 0
    flag = 1
    i = 0
    while i < (len(roman_string) - 1):
        if symbols[roman_list[i]] < symbols[roman_list[i + 1]]:
            num += symbols[roman_list[i + 1]] - symbols[roman_list[i]]
            i += 2
            flag = 0
        else:
            num += symbols[roman_list[i]]
            flag = 1
            i += 1
    if flag == 1:
        num += symbols[roman_list[-1]]
    return num
