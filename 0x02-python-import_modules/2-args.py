#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    values = sys.argv[1:]
    if len(values) == 0:
        print("{} arguments.".format(len(values)))
    else:
        if len(values) == 1:
            print("{} argument:".format(len(values)))
        else:
            print("{} arguments:".format(len(values)))
        for i, val in enumerate(values):
            i += 1
            print("{}: {}".format(i, val))
