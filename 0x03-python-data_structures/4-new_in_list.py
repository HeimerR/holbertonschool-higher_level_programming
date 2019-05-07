def new_in_list(my_list, idx, element):
    local = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        local[idx] = element
        return local
