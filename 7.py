import numpy as np

matrix_original = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

finish_sum = np.sum(matrix_original)
row_sum = np.sum(matrix_original, axis=1)
proportions = row_sum / finish_sum

matrix_new = np.zeros((matrix_original.shape[0], matrix_original.shape[1]+1))
matrix_new[:,:matrix_original.shape[1]] = matrix_original
matrix_new[:,-1] = proportions

print(matrix_new)