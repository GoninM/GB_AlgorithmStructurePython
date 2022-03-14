# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random


def find_2_minimums(input_list):
    min1 = input_list[0]
    min2 = input_list[0]

    for item in input_list:
        if item <= min1:
            min2 = min1
            min1 = item
        elif item <= min2:
            min2 = item

    return min1, min2


test_data = [random.randint(-100, 100) for _ in range(5)]
test_data_2 = [-11, -11, -10, 0, 1]
test_data_3 = [67, 12, -30, -50, -46]

print(f'2 минимума для: {test_data}')
print(f'min1 = {find_2_minimums(test_data)[0]} min2 = {find_2_minimums(test_data)[1]}')

print('-'*30)

print(f'2 минимума для: {test_data_2}')
print(f'min1 = {find_2_minimums(test_data_2)[0]} min2 = {find_2_minimums(test_data_2)[1]}')

print('-'*30)

print(f'2 минимума для: {test_data_3}')
print(f'min1 = {find_2_minimums(test_data_3)[0]} min2 = {find_2_minimums(test_data_3)[1]}')
