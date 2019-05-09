#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    roman_list = list(roman_string)
    num = 0
    flag = 1
    for i in range(len(roman_string) - 1):
        if symbols[roman_list[i]] < symbols[roman_list[i + 1]]:
            num += symbols[roman_list[i + 1]] - symbols[roman_list[i]]
            i = i + 1
            flag = 0
        else:
            num += symbols[roman_list[i]]
            flag = 1
    if flag == 1:
        num += symbols[roman_list[-1]]
    return num
