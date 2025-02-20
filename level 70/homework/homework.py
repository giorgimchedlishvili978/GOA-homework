def generate_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]  # ვქმნით ნულოვან მატრიცას
    current = 1  # დასაწყისი რიცხვი
    for col in range(m):
        for row in range(n):
            matrix[row][col] = current
            current += 1
    return matrix
