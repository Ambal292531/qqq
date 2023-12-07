import numpy as np

def qqq(A):
    # Нормируем элементы каждого столбца по отношению к наибольшему элементу этого столбца
    normalized_columns = A / np.max(A, axis=0)

    return normalized_columns


# Пример использования
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

test = qqq(A)
print(test)