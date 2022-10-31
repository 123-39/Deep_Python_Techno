"""
matrix multiplication
"""
import ctypes
import random
import os

CHAIN_LEN = 100
MATRIX_SIZE = 60


def c_matrix_chain_mul(matrix_chain):
    """ C matrix chain multiplication """

    n_matrix = len(matrix_chain)
    size = len(matrix_chain[0])

    matrixes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_int)) * n_matrix)()
    for i in range(n_matrix):
        matrixes[i] = (ctypes.POINTER(ctypes.c_int) * size)()
        for j in range(size):
            matrixes[i][j] = (ctypes.c_int * size)(*matrix_chain[i][j])

    output = (ctypes.POINTER(ctypes.c_int) * size)()
    for i in range(size):
        output[i] = (ctypes.c_int * size)()

    lib = ctypes.cdll.LoadLibrary(os.path.abspath('libmatmul.so'))

    matrix_mult = lib.matrix_chain_mul
    matrix_mult(ctypes.byref(matrixes), output, n_matrix, size)

    matrix_output = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(output[i][j])
        matrix_output.append(row)

    return matrix_output


def py_matrix_mul(left_matrix, right_matrix, size):
    """ Python matrix multiplication"""

    result = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += left_matrix[i][k] * right_matrix[k][j]

    return result


def py_matrix_chain_mul(matrix_chain):
    """ Python matrix chain multiplication """

    n_matrix = len(matrix_chain)
    size = len(matrix_chain[0])

    result = matrix_chain[0]

    for idx in range(1, n_matrix):
        result = py_matrix_mul(result, matrix_chain[idx], size)

    return result


def matrix_generate(n_matrix=2, size=2):
    """
    square matrixes generation
    """

    if n_matrix < 1:
        raise Exception('Number of matrix < 1')

    matrixes = []

    for _ in range(n_matrix):
        one_matrix = []
        for _ in range(size):
            col = []
            for _ in range(size):
                col.append(random.randint(-10, 10))
            one_matrix.append(col)
        matrixes.append(one_matrix)

    return matrixes
