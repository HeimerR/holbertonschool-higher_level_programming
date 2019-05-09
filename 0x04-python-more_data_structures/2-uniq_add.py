#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        sum = 0
        my_list.sort()
        for i in my_list:
            while my_list.count(i) > 1:
                my_list.remove(i)
            sum += i
        return sum
