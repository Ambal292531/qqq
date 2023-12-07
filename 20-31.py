#20
def parallel_diagonal_product(matrix):
    product = 1
    n = len(matrix)
    for i in range(n):
        product *= matrix[i][n-i-1]
    return product

#21
def symmetrical_values(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            avg = (matrix[i][j] + matrix[j][i]) / 2
            matrix[i][j] = avg
            matrix[j][i] = avg

#22
def make_even_ones(matrix):
    for row in matrix:
        if row.count(1) % 2 != 0:
            row.append(1)
        else:
            row.append(0)


#23
def sum_and_product_above_diagonals(matrix):
    n = len(matrix)
    sum_above_main = sum(matrix[i][j] for i in range(n) for j in range(i+1, n))
    product_above_secondary = 1
    for i in range(n):
        product_above_secondary *= matrix[i][n-i-1]
    return sum_above_main, product_above_secondary

#24
def split_and_sum(matrix, l, k):
    n = len(matrix)
    m = len(matrix[0])
    sum1 = sum(matrix[i][j] for i in range(l) for j in range(k))
    sum2 = sum(matrix[i][j] for i in range(l) for j in range(k, m))
    sum3 = sum(matrix[i][j] for i in range(l, n) for j in range(k))
    sum4 = sum(matrix[i][j] for i in range(l, n) for j in range(k, m))
    return sum1, sum2, sum3, sum4

#25
def count_zeros(matrix):
    result = []
    for row in matrix:
        result.append(row.count(0))
    transposed_matrix = list(zip(*matrix))
    for col in transposed_matrix:
        result.append(col.count(0))
    return result

#26
def average_of_parts(matrix, l, k):
    n = len(matrix)
    m = len(matrix[0])
    part1 = [matrix[i][j] for i in range(l) for j in range(k)]
    part2 = [matrix[i][j] for i in range(l) for j in range(k, m)]
    part3 = [matrix[i][j] for i in range(l, n) for j in range(k)]
    part4 = [matrix[i][j] for i in range(l, n) for j in range(k, m)]
    avg1 = sum(part1) / len(part1)
    avg2 = sum(part2) / len(part2)
    avg3 = sum(part3) / len(part3)
    avg4 = sum(part4) / len(part4)
    return avg1, avg2, avg3, avg4

#27
def check_number_in_rows(matrix, n):
    result = []
    for row in matrix:
        if n in row:
            result.append("Contains")
        else:
            result.append("Does not contain")
    return result

#28
def exclude_and_concat(matrix, l):
    result = [row[:l] + row[l+1:] for row in matrix]
    return [list(x) for x in zip(*result)]

#29
def add_and_insert_column(matrix, l, new_column):
    result = [row[:l] + [new_column] + row[l:] for row in matrix]
    return result

#30
def balance_column_sum(matrix):
    result = []
    for col in zip(*matrix):
        positive_sum = sum(x for x in col if x > 0)
        negative_sum = abs(sum(x for x in col if x < 0))
        new_element = negative_sum - positive_sum
        col = list(col)
        col.append(new_element)
        result.append(col)
    return result

#31
def balance_row_sum(matrix):
    result = []
    for row in matrix:
        positive_sum = sum(x for x in row if x > 0)
        negative_sum = abs(sum(x for x in row if x < 0))
        new_element = negative_sum - positive_sum
        row.append(new_element)
        result.append(row)
    return result

#32

