def q_min_colichestvo(matrix):
    max_sum = 0
    min_col_element = None
    
    for col in range(len(matrix[0])):
        sum = 0
        min_element = float('inf')
        
        for row in range(len(matrix)):
            sum += abs(matrix[row][col])
            
            if sum > max_sum:
                min_element = matrix[row][col]
                
        if sum > max_sum:
            max_sum = sum
            min_col_element = min_element
    return min_col_element
matrix = [
    [1, -2, 3],
    [4, -5, 6],
    [-7, 8, 9]
]

test = q_min_colichestvo(matrix)
print(test)
            
            