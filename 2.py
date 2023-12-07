def max(matrix):
    max_avg = float('-inf')

    for row in matrix:
        avg = sum(row) / len(row)

        if avg > max_avg:
            max_avg = avg
    return max_avg

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test = max(matrix)
print(test)