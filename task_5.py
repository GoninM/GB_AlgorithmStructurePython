# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random


def find_index_max_negative_element(input_list):
    index = -1

    for item in input_list:
        if item < 0 and index == -1:
            index = input_list.index(item)
        elif item < 0:
            if abs(item) < abs(input_list[index]):
                index = input_list.index(item)
        else:
            pass

    return index


test_data_1 = [random.randint(-100, 100) for _ in range(5)]

print(test_data_1)

i = find_index_max_negative_element(test_data_1)

if i == -1:
    print(f'элемент не найден')
else:
    v = test_data_1[i]
    print(f'position = {i: 3}: value = {v: > 4}')

