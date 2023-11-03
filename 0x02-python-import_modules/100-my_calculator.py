#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    argv_len = len(argv) - 1
    return_val = 0
    if argv_len != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    match argv[2]:
        case "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        case "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        case "*":
             print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        case "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)
