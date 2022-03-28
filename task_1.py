# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

LOW_LIMIT = -100
UP_LIMIT = 100
# ARRAY_SIZE = 200

test_array = [_ for _ in range(LOW_LIMIT, UP_LIMIT)]
random.shuffle(test_array)
print(f'input: {test_array}')


def sort_bubble(array):
    # step = 1
    for i in range(len(array)-1, -1, -1):
        for j in range(len(array)-1, len(array)-i-1, -1):
            if array[j] > array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

        # print(f'step {step} : {array}')
        # step += 1


sort_bubble(test_array)
print(f'output: {test_array}')
