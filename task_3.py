# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

#version 1
min_value = 100
max_value = 0

input_list = [random.randint(max_value, min_value) for _ in range(10)]
print('Input list:')
print(input_list)

index_min = 0
index_max = 0

for item in input_list:
    if item < min_value:
        min_value = item
        index_min = input_list.index(item)
    if item > max_value:
        max_value = item
        index_max = input_list.index(item)

print(f'min = {min_value}, max = {max_value}')

input_list[index_min], input_list[index_max] = input_list[index_max], input_list[index_min]

print('Result list:')
print(input_list)

#version 2
min_value = 100
max_value = 0
index_min = 0
index_max = 0


for i in range(len(input_list)):
    if input_list[i] > max_value:
        max_value = input_list[i]
        index_max = i
    if input_list[i] < min_value:
        min_value = input_list[i]
        index_min = i

print(f'min = {min_value}, max = {max_value}')

input_list[index_min], input_list[index_max] = input_list[index_max], input_list[index_min]

print('Result list, version2:')
print(input_list)
