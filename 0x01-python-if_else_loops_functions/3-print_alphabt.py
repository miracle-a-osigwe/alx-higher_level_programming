#!/usr/bin/python3
for x in range(97, 97+26):
    if chr(x) in "qe":
        continue
    else:
        print("{}".format(chr(x)), end="")
