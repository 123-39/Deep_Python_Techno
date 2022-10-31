"""
matrix chain multiplication tests
"""
import unittest
import time

from matrix_multiplication import c_matrix_chain_mul, py_matrix_chain_mul, matrix_generate


class TestMatrixMultiplication(unittest.TestCase):

    def test_correct_py_multiplication(self):

        matrixes = [
            [[1, 2], [3, 4]],
            [[42, 15], [23, 13]],
        ]

        result = py_matrix_chain_mul(matrixes)

        self.assertListEqual(result, [[88, 41], [218, 97]])

    def test_correct_c_multiplication(self):

        matrixes = [
            [[1, 2], [3, 4]],
            [[42, 15], [23, 13]],
        ]

        result = c_matrix_chain_mul(matrixes)

        self.assertListEqual(result, [[88, 41], [218, 97]])

    def test_speed(self):

        CHAIN_LEN = 50
        MATRIX_SIZE = 40

        matrixes = matrix_generate(CHAIN_LEN, MATRIX_SIZE)

        start = time.time()
        py_matrix_chain_mul(matrixes)
        py_time = time.time() - start

        start = time.time()
        c_matrix_chain_mul(matrixes)
        c_time = time.time() - start

        self.assertLess(c_time, py_time)

    def test_zero_matrix_generation(self):

        CHAIN_LEN = 0
        MATRIX_SIZE = 40

        with self.assertRaises(Exception):
            _ = matrix_generate(CHAIN_LEN, MATRIX_SIZE)

if __name__ == '__main__':

    unittest.main()
