def print_reversed_list_integer(my_list=[]):
    local = my_list.copy()
    local.reverse()
    for i in range(len(local)):
        print("{:d}".format(local[i]))
