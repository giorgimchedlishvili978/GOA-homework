def print_positions(rows, cols):
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            print(f"row: {r} col: {c}")


def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = [i * j for j in range(1, n + 1)]
        table.append(row)
    return table


def print_pairs(n):
    pairs = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > i:
                pairs.append((i, j))
    return pairs

# მაგალითი
result_pairs = print_pairs(3)
for pair in result_pairs:
    print(pair)
