# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random


def find_mediana(array, k):
    # print(f'arr = {array}')
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)
    # print(f'pivot = {pivot} k = {k}')

    l_array = []
    r_array = []
    m_array = []

    for item in array:
        if item < pivot:
            l_array.append(item)
        elif item > pivot:
            r_array.append(item)
        else:
            m_array.append(item)

    # print(f'l:{l_array} r:{r_array} m:{m_array}')

    if k < len(l_array):
        return find_mediana(l_array, k)
    elif k < len(l_array) + len(m_array):
        return m_array[0]
    else:
        return find_mediana(r_array, k - len(l_array) - len(m_array))


M = 10
size = 2*M + 1

LOW_LIMIT = 0
UP_LIMIT = 100

test_array = [random.randint(LOW_LIMIT, UP_LIMIT) for _ in range(size)]

print(test_array)
print(f'result = {find_mediana(test_array, M)}')

test_array.sort()
print(test_array)
print(f'check result = {test_array[M]}')



