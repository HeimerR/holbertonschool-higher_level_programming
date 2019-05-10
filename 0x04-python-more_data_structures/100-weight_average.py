#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is [] or my_list is None:
        return 0
    num = 0
    den = 0
    for i in range(len(my_list)):
        num += my_list[i][0] * my_list[i][1]
        den += my_list[i][1]
    return num/den
