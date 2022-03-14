# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


def find_min_in_column(input_matrix):
    rows = len(input_matrix)
    columns = len(input_matrix[0])

    result = []

    for j in range(columns):
        min = input_matrix[0][j]
        for i in range(rows):
            if matrix[i][j] < min:
                min = matrix[i][j]
        result.append(min)

    return result


def find_max(input_list):
    max = input_list[0]
    for item in input_list:
        if item > max:
            max = item

    return max


def print_matrix(input_matrix):
    for row in input_matrix:
        r = ''
        for item in row:
            r += f'{item: 4}'
        print(r)


# create matrix
size_rows = 4
size_columns = 5

matrix = [[random.randint(-10, 10) for _ in range(size_columns)] for j in range(size_rows)]

print(f'input matrix:')
print_matrix(matrix)
print('----'*size_columns)

minimums = find_min_in_column(matrix)
print(f'minimums in columns:')
str = ''
for item in minimums:
    str += f'{item: 4}'
print(str)
print('----'*size_columns)

print(f'max from min in columns = {find_max(minimums)}')
