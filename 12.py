import numpy as np


def qqq(A):
    normalized_rows = A / np.max(A, axis=1)[:, None]

    return normalized_rows



A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

test = qqq(A)
print(test)