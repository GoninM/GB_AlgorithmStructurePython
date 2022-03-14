# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
# используйте один любой по вашему выбору.


#не очень вариант

import random


def find_min_max_position(input_list):
    i_min = 0
    i_max = 0

    for i in range(1, len(input_list)):
        if input_list[i] < input_list[i_min]:
            i_min = i

        if input_list[i] > input_list[i_max]:
            i_max = i

    return i_min, i_max


def find_sum(input_list, i_min, i_max):
    result = 0

    for i in range(0, len(input_list)):
        if input_list[i_min] < input_list[i] < input_list[i_max]:
            result += input_list[i]

    return result


test_data = [random.randint(-50, 50) for _ in range(5)]
print(test_data)

pos_min, pos_max = find_min_max_position(test_data)
sum = find_sum(test_data, pos_min, pos_max)
print(f"pos_min = {pos_min} | pos_max = {pos_max} | sum = {sum}")
