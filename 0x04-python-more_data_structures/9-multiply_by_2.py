#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict:
        value = new_dict[key]
        new_dict[key] = value * 2
    return new_dict
