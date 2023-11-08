#!/usr/bin/python3

matrix = [[1,2,3], [4,5,6]]
new_matrix = []

for row in matrix:
    new_matrix.append(list(map(lambda x: x ** 2, row)))

print(new_matrix)
