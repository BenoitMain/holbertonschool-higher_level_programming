#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
