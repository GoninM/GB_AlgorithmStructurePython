# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random
import cProfile


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


# def main():
test_data_1 = [random.randint(-100, 100) for _ in range(1000)]
find_index_max_negative_element(test_data_1)


# cProfile.run('main()')

# n = 100
# 628 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:17(find_index_max_negative_element)

# n = 500
# 3158 function calls in 0.002 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:17(find_index_max_negative_element)

# n = 1000
# 6220 function calls in 0.003 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:17(find_index_max_negative_element)
# 926    0.000    0.000    0.000    0.000 {built-in method builtins.abs}

# 100 loops, best of 5: 9 nsec per loop
# 200 loops, best of 5: 10 nsec per loop
# 1000 loops, best of 5: 11.2 nsec per loop
# 10000 loops, best of 5: 10.6 nsec per loop
