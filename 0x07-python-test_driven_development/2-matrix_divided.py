#!/usr/bin/python3

""" Defines a function matrix_divided """

def matrix_divided(matrix, div):
    """ divide every element of a matrix by a number and returns a new matrix
        containing the results of the divisions 

    Args:
        matrix (list): This is a list of lists and containing integers/floats
            that are divided by `div`
        div (int/float): divides the elements of `matrix`

    Returns:
        list: a new list if successful

    Raises:
        TypeError: If `matrix` is not a list of lists
            If outer list of `matrix` is empty
            If an inner list of `matrix` is empty
            If inner lists of `matrix` are not the same sizes
            If an element of a list is not an integer or float
            If `div` is not an integer or float

        ZeroDivisionError: If `div` is 0
    """
 
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
