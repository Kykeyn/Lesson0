def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for b in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input(f'Введите колличество строк: '))
m = int(input(f"Введите колличество столбцов: "))
value = input(f'Введите значения: ')
matrix = get_matrix(n, m, value)

