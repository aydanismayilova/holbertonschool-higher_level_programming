#!/usr/bin/python3
for c in range(97, 123):
    print("{}".format(chr(c)) if chr(c) not in "qe" else "", end="")
