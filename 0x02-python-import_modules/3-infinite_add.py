#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    values = [int(x) for x in sys.argv[1:]]
    print("{}".format(sum(values)))
