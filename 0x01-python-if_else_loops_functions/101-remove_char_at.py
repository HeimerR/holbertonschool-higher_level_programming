#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = []
    if(n >= 0):
        for i in range(len(str)):
            if(i != n):
                str2.append(str[i])
        str1 = ''.join(str2)
        return(str1)
    return(str)
