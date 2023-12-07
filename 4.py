def q_avg(matrix):
    min_avg = float('inf')
    
    for row in matrix:
        avg = sum(row) / len(row)
        
        if avg < min_avg:
            min_avg = avg
            
    return min_avg

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test = q_avg(matrix)
print(test)
