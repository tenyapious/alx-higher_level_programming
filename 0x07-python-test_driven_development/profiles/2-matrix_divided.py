#!/usr/bin/python3

@profile
def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    first_row_len = len(matrix[0])

    for row in matrix:
        new_row = []
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for ele in row:
                if isinstance(ele, (int, float)):
                    new_row.append(round((ele / div), 2))
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(new_row)

    return new_matrix
matrix_divided([[1,2,3],[4,5,6]], 3)
