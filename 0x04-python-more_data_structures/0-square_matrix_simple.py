#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    computed = []
    for row in matrix:
        add = []
        for col in row:
            add.append(col*col)
        computed.append(add)
    return computed
