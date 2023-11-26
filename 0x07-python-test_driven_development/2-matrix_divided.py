#!/usr/bin/python3

def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
 
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
       
        for ele in row:
            if isinstance(ele, (int, float)):
                new_row.append(round((ele / div), 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if len(new_row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(new_row)

    if len(new_matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return new_matrix
