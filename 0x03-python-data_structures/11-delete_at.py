def delete_at(my_list=[], idx=0):
    if my_list is not None:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            del my_list[idx:idx+1]
            return my_list
