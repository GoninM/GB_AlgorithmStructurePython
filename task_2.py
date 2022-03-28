# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):
    # print(f'input = {array}')

    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        l_copy = merge_sort(array[:mid])
        r_copy = merge_sort(array[mid:])

        result = []
        l_index = 0
        r_index = 0
        while l_index < len(l_copy) and r_index < len(r_copy):
            if l_copy[l_index] < r_copy[r_index]:
                result.append(l_copy[l_index])
                l_index += 1
            else:
                result.append(r_copy[r_index])
                r_index += 1

        while l_index < len(l_copy):
            result.append(l_copy[l_index])
            l_index += 1

        while r_index < len(r_copy):
            result.append(r_copy[r_index])
            r_index += 1

        # print(f'return result = {result}')

        return result


LOW_LIMIT = -50
UP_LIMIT = 50
SIZE = 7

test_array = [random.uniform(LOW_LIMIT, UP_LIMIT) for _ in range(SIZE)]
# test_array = [random.randint(LOW_LIMIT, UP_LIMIT) for _ in range(SIZE)]
# test_array = [_ for _ in range(SIZE)]
# random.shuffle(test_array)

print(f'in: {test_array}')
print(f'out: {merge_sort(test_array)}')
