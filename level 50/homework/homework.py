def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


matrix1 = [[1, 3], [1, 4]]
matrix2 = [[4, 1], [2, 2]]
result = add_matrices(matrix1, matrix2)
print(result)  # [[5, 4], [3, 6]]


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_matrix(matrix)
print(transposed)  # [[1, 4], [2, 5], [3, 6]]


def diagonal_sum(matrix):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(matrix)
    
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]
    
    return primary_diagonal_sum, secondary_diagonal_sum


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonal_sum(matrix)
print(result)  # (15, 15)
