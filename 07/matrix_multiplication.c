#include "matrix_multiplication.h"

void matr_copy(int **left_matrix, int **right_matrix, int size) {

    for (int i = 0; i <  size; ++i) {
        for (int j = 0; j <  size; ++j) {
            right_matrix[i][j] = left_matrix[i][j];
        }
    }
}

void multiply(int **left_matr, int **right_matr, int **result, int size) {

    for(int i = 0; i < size; i++) {
        for(int j = 0; j < size; j++) {
            result[i][j] = 0;
            for(int k = 0; k < size; k++) {
                result[i][j] += left_matr[i][k] * right_matr[k][j];
            }
        }
    }
}

int **matrix_chain_mul(int ***matrix_chain, int **result, int n_matrix, int size) {

    int **tmp = (int **) malloc(size * sizeof(int*));
    for (int i = 0; i < size; ++i) {
        tmp[i] = (int *) malloc(size * sizeof(int));
    }

    matr_copy(matrix_chain[0], tmp, size);

    for (int i = 0; i < n_matrix - 1; ++i) {
        multiply(tmp, matrix_chain[i + 1], result, size);
        matr_copy(result, tmp, size);
    }

    for (int i = 0; i < size; ++i) {
        free(tmp[i]);
    }

    free(tmp);
    return result;

}