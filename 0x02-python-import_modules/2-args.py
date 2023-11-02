#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_len = len(argv) - 1

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argv_len))
        for i in range(1, argv_len + 1):
            print("{}: {}".format(i, argv[i]))
