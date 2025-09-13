def matrix_diagonal(matrix, value):

    if len(matrix) == 0 or abs(value) >= len(matrix[0]) or abs(value) >= len(matrix):
        return

    new_matrix = []

    i = 0
    j = 0

    limit = len(matrix) - abs(value)
    while limit != 0:
        m_value = matrix[value + i][j] if value > 0 else matrix[i][abs(value) + j]
        new_matrix.append(m_value)
        i += 1
        j += 1
        limit -= 1

    return sum(new_matrix)


def sum_diagonals(matrix):
    if len(matrix) == 0:
        return 0

    sum_d = 0
    step = 1
    i = 0
    j = 0

    while i < len(matrix):
        sum_d += matrix[i][j]
        i += 1
        j += 1
        if i == len(matrix) and step == 1:
            i = 0
            j = 0
            matrix = matrix[::-1]
            step += 1

    return sum_d


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def gcd_matrix(a, b):
    gcd_arr = []
    n, m = len(a), len(b)
    count_matrix = n * m
    for i in range(m):
        row = []
        for j in range(n):
            row.append(gcd(a[j], b[i]))
        gcd_arr.append(row)

    sum_matrix = sum(sum(raw) for raw in gcd_arr)

    return round(sum_matrix / count_matrix, 3)


matrix = [
    [-2, 5, 3, 2],
    [9, -6, 5, 1],
    [3, 2, 7, 3],
    [-1, 8, -4, 8],
]

a = [1, 2, 3]
b = [4, 5, 6]

print(gcd_matrix(a, b))
