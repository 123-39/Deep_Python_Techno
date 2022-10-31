#ifndef _MATRIX_MULTIPLICATION_H
#define _MATRIX_MULTIPLICATION_H


#include <stdlib.h>

void multiply_c(int **left, int **right, int **result, int size);

int **matrix_chain_mul(int ***matrix_sequence, int **result, int seq_size, int size);

void copy(int **left,int **right, int size);


#endif // _MATRIX_MULTIPLICATION_H