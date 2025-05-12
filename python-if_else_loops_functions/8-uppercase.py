#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            str_uppercase = chr(ord(c) - 32)

        else:
            str_uppercase = c
        print("{}".format(str_uppercase), end="")
    print()
