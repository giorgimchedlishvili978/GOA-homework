def sum_and_average(matrix):
    row_sums = []
    row_averages = []
    
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)  
        row_averages.append(row_sum / len(row)) 
    
    return row_sums, row_averages

# მაგალითად გამოყენება
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums, row_averages = sum_and_average(matrix)

print("Row sums:", row_sums)
print("Row averages:", row_averages)
