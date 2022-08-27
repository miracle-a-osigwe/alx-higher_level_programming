#!/usr/bin/python3

from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    import sys
    args = sys.argv[0:]
    if len(args) < 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    operator = args[2]

    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, int(div(a, b))))
    else:
        result = "Unknown operator. Available operators: +, -, * and /"
        print("{}".format(result))
        sys.exit(1)
