import numpy as np

def qqq(A, K):
    multiplied_columns = A * A[:, K - 1][:, None]

    return multiplied_columns


A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

test = qqq(A, 2)
print(test)