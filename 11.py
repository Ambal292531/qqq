import numpy as np

def qqq(A, L):
    # Суммируем элементы каждой строки с соответствующими элементами L-той строки
    summed_rows = A + A[L - 1]

    return summed_rows


# Пример использования
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

test = qqq(A, 2)
print(test)