#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1

    argv_len = len(argv) - 1
    return_val = 0
    if argv_len != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    match argv[2]:
        case "+":
            print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
        case "-":
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
        case "*":
             print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
        case "/":
            print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)
