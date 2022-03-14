# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# create empty matrix
size_rows = 4
size_columns = 5

matrix = [[[] for _ in range(size_columns)] for j in range(size_rows)]

# fill matrix
for i in range(size_rows):
    sum = 0
    for j in range(size_columns):
        if j == size_columns - 1:
            matrix[i][j] = sum
        else:
            matrix[i][j] = int(input(f'введите значение элемента a{i}{j}: '))
            sum += matrix[i][j]

for item in matrix:
    print(item)

