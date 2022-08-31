#!/usr/bin/python3

def search_replace(my_list, search, replace):
    try:
        loc = my_list.index(search)
        new_list = my_list.copy()
        new_list.pop(loc)
        new_list.insert(loc, replace)
        return new_list
    except Exception as e:
        return None
