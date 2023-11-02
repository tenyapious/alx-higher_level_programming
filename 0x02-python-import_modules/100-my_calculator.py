#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    def my_calculator():
        argv_len = len(argv) - 1
        if argv_len != 3:
            print("Usage: {} <a> <operator> <b>".format(argv[0]))
            return (1)

        a = int(argv[1])
        b = int(argv[3])

        match argv[2]:
            case "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            case "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            case "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            case "/":
                print("{} / {} = {}".format(a, b, div(a, b)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                return (1)
        return (0)

    my_calculator()
