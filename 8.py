import numpy as np

def q_matrix(matrix_a):
    col_negativ = np.sum(matrix_a < 0, axis=0)
    row_negativ = np.sum(matrix_a < 0, axis=0)

    matrix_c = np.zeros((matrix_a.shape[0]+1, matrix_a.shape[1]+1))
    matrix_c[:matrix_a.shape[0], :matrix_a.shape[1]] = matrix_a
    matrix_c[:matrix_a.shape[0], -1] = row_negativ
    matrix_c[-1,:matrix_a.shape[1]] = col_negativ

    return matrix_c

matrix_a = np.array([
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]])
test = q_matrix(matrix_a)
print(test)