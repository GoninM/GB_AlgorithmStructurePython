# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random


def find_mediana(array):
    min_value = array[0]
    max_value = array[0]

    for item in array:
        if item < min_value:
            min_value = item
        if item > max_value:
            max_value = item

    mid = (max_value+min_value)//2
    print(f'min = {min_value} max = {max_value} mid = {mid}')

    counter = 0
    mediana = 0

    for item in array:
        if item < mid:
            counter += 1
            if mediana < item:
                mediana = item

            print(f'{item} < {mid} counter = {counter} mediana = {mediana}')

        if counter > len(array)//2:
            if
            mediana = item
            break

    print(f'counter = {counter} mediana = {mediana}')


M = 2
size = 2*M + 1

LOW_LIMIT = 0
UP_LIMIT = 100

test_array = [random.randint(LOW_LIMIT, UP_LIMIT) for _ in range(size)]

print(test_array)
find_mediana(test_array)


