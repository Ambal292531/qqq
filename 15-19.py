# 15. Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.

def check_columns(matrix, number):
    n = len(matrix)
    m = len(matrix[0])
    columns_with_number = []
    columns_without_number = []
    for j in range(m):
        has_number = False
        for i in range(n):
            if matrix[i][j] == number:
                has_number = True
                break
        if has_number:
            columns_with_number.append(j)
        else:
            columns_without_number.append(j)
    return columns_with_number, columns_without_number


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
number = 3
columns_with_number, columns_without_number = check_columns(matrix, number)
print(columns_with_number)
print(columns_without_number)

# 16. Исключить из матрицы строку с номером L. Сомкнуть строки матрицы.

def exclude_row(matrix, l):
    del matrix[l]
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
l = 1
result = exclude_row(matrix, l)
print(result)  # Вывод: [[1, 2, 3], [7, 8, 9]] (исключена строка с индексом 1)

# 17. Добавить к матрице строку и вставить ее под номером L.

def add_row(matrix, row, l):
    matrix.insert(l, row)
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_row = [10, 11, 12]
l = 1
result = add_row(matrix, new_row, l)
print(result)  # Вывод: [[1, 2, 3], [10, 11, 12], [4, 5, 6], [7, 8, 9]] (

# 18. Найти сумму элементов, стоящих на главной диагонали и на побочной диагонали

def sum_diagonals(matrix):
    n = len(matrix)
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    side_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))
    return main_diagonal_sum, side_diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
main_sum, side_sum = sum_diagonals(matrix)
print(main_sum)
print(side_sum)

# 19. Определить сумму элементов, расположенных параллельно главной диагонали (ближайшие к главной).

def sum_parallel_to_main_diagonal(matrix):
    n = len(matrix)
    parallel_sum = sum(matrix[i][j] for i in range(n) for j in range(i))
    return parallel_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = sum_parallel_to_main_diagonal(matrix)
print(result)     #(сумма элементов параллельно главной диагонали: 2 + 4 + 3 + 7)