#!/usr/bin/python3

class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    def calcSq(self):
        return (int(self.__height) * int(self.__width))

def main():
    square = Square()

    height = input("Enter a height: ")
    width = input("Enter a width: ")

    square.height = height
    square.width = width

    print(square.height)

    square.calcSq()

main()
