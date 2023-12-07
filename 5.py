import numpy as np

#создадим матрицу
matrix_original = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

#идется вычисление по line и по column

avg_rows = np.mean(matrix_original, axis=1)
avg_cols = np.mean(matrix_original, axis=0)
avg_all = np.mean(matrix_original)

#создание новой матрицы

matrix_new = np.zeros((matrix_original.shape[0]+1, matrix_original.shape[1]+1))
matrix_new[:matrix_original.shape[0], :matrix_original.shape[1]] = matrix_original
matrix_new[matrix_original.shape[0], :matrix_original.shape[1]] = avg_rows
matrix_new[:matrix_original.shape[0], matrix_original.shape[1]] = avg_cols
matrix_new[matrix_original.shape[0], matrix_original.shape[1]] = avg_all

print(matrix_new)