import numpy as np

def q_matrix(matrix_A, matrix_L, matrix_K):
    zero_elem_row = np.sum(matrix_A[:matrix_L,:] == 0)
    zero_elem_column = np.sum(matrix_A[:,:matrix_K] == 0)

    new_matrix_D = np.zeros((matrix_A.shape[0]+1, matrix_A.shape[1]+1))
    new_matrix_D[:matrix_A.shape[0], :matrix_A.shape[1]] = matrix_A
    new_matrix_D[:matrix_L, -1] = zero_elem_column
    new_matrix_D[-1, :matrix_K] = zero_elem_column

    return new_matrix_D

matrix_A = np.array([
    [0, 2, 3],
    [0, 5, 6],
    [7, 8, 9]
])

test = q_matrix(matrix_A, matrix_L, matrix_K)
print(test)
