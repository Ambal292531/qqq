def max(matrix):
    max_sum = 0
    max_element = None
    for colichestvo in range(len(matrix[0])):
        colichestvo_sum = 0

        for stroka in range(len(matrix)):
            colichestvo_sum += abs(matrix[stroka][colichestvo])

        if colichestvo_sum > max_sum:
            max_sum = colichestvo_sum
            max_element = matrix[stroka][colichestvo]

    return max_element
matrix = [
    [1, -2, -3],
    [4, -5, 6],
    [-7, 8, 9]
]

test = max(matrix)
print(test)