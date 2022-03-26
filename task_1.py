# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл.
# Рекомендуем использовать английские имена, например, les_6_task_1, les_6_task_2, и т.д.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
#
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.




# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import sys
import ctypes
import struct


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size = {sys.getsizeof(x)}, object={x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


print(sys.version, sys.platform)
# 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32

# create empty matrix
size_rows = 4
size_columns = 5

show_size(size_rows)
show_size(size_columns)

# type=<class 'int'>, size = 14, object=4
# type=<class 'int'>, size = 14, object=5

print(id(size_rows))
print(ctypes.string_at(id(size_rows), sys.getsizeof(size_rows)))
print(struct.unpack('LLLcc', ctypes.string_at(id(size_rows), sys.getsizeof(size_rows))))
print(id(size_columns))
print(ctypes.string_at(id(size_columns), sys.getsizeof(size_columns)))
print(struct.unpack('LLLcc', ctypes.string_at(id(size_columns), sys.getsizeof(size_columns))))

# 2051074016
# b'8\x00\x00\x00(\x81?z\x01\x00\x00\x00\x04\x00'
# (56, 2050982184, 1, b'\x04', b'\x00')
# 2051074032
# b'!\x00\x00\x00(\x81?z\x01\x00\x00\x00\x05\x00'
# (33, 2050982184, 1, b'\x05', b'\x00')

print(id(int))
# 2050982184


matrix = [[[] for _ in range(size_columns)] for j in range(size_rows)]
show_size(matrix)


# type=<class 'list'>, size = 44, object=[[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
# 	 type=<class 'list'>, size = 60, object=[[], [], [], [], []]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 	 type=<class 'list'>, size = 60, object=[[], [], [], [], []]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 	 type=<class 'list'>, size = 60, object=[[], [], [], [], []]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 	 type=<class 'list'>, size = 60, object=[[], [], [], [], []]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
# 		 type=<class 'list'>, size = 28, object=[]
#

# fill matrix
for i in range(size_rows):
    sum = 0
    for j in range(size_columns):
        if j == size_columns - 1:
            matrix[i][j] = sum
        else:
            matrix[i][j] = int(input(f'введите значение элемента a{i}{j}: '))
            sum += matrix[i][j]

show_size(matrix)

 # type=<class 'list'>, size = 44, object=[[1, 2, 3, 4, 10], [5, 6, 7, 8, 26], [9, 0, 0, 9, 18], [8, 7, 6, 5, 26]]
	#  type=<class 'list'>, size = 60, object=[1, 2, 3, 4, 10]
	# 	 type=<class 'int'>, size = 14, object=1
	# 	 type=<class 'int'>, size = 14, object=2
	# 	 type=<class 'int'>, size = 14, object=3
	# 	 type=<class 'int'>, size = 14, object=4
	# 	 type=<class 'int'>, size = 14, object=10
	#  type=<class 'list'>, size = 60, object=[5, 6, 7, 8, 26]
	# 	 type=<class 'int'>, size = 14, object=5
	# 	 type=<class 'int'>, size = 14, object=6
	# 	 type=<class 'int'>, size = 14, object=7
	# 	 type=<class 'int'>, size = 14, object=8
	# 	 type=<class 'int'>, size = 14, object=26
	#  type=<class 'list'>, size = 60, object=[9, 0, 0, 9, 18]
	# 	 type=<class 'int'>, size = 14, object=9
	# 	 type=<class 'int'>, size = 12, object=0
	# 	 type=<class 'int'>, size = 12, object=0
	# 	 type=<class 'int'>, size = 14, object=9
	# 	 type=<class 'int'>, size = 14, object=18
	#  type=<class 'list'>, size = 60, object=[8, 7, 6, 5, 26]
	# 	 type=<class 'int'>, size = 14, object=8
	# 	 type=<class 'int'>, size = 14, object=7
	# 	 type=<class 'int'>, size = 14, object=6
	# 	 type=<class 'int'>, size = 14, object=5
	# 	 type=<class 'int'>, size = 14, object=26


for item in matrix:
    print(item)


matrix_tuple = []
for item in matrix:
    matrix_tuple.append(tuple(item))
matrix_tuple = tuple(matrix_tuple)

show_size(matrix_tuple)

 # type=<class 'tuple'>, size = 36, object=((1, 2, 3, 4, 10), (5, 6, 7, 8, 26), (9, 0, 9, 8, 26), (7, 6, 5, 4, 22))
	#  type=<class 'tuple'>, size = 40, object=(1, 2, 3, 4, 10)
	# 	 type=<class 'int'>, size = 14, object=1
	# 	 type=<class 'int'>, size = 14, object=2
	# 	 type=<class 'int'>, size = 14, object=3
	# 	 type=<class 'int'>, size = 14, object=4
	# 	 type=<class 'int'>, size = 14, object=10
	#  type=<class 'tuple'>, size = 40, object=(5, 6, 7, 8, 26)
	# 	 type=<class 'int'>, size = 14, object=5
	# 	 type=<class 'int'>, size = 14, object=6
	# 	 type=<class 'int'>, size = 14, object=7
	# 	 type=<class 'int'>, size = 14, object=8
	# 	 type=<class 'int'>, size = 14, object=26
	#  type=<class 'tuple'>, size = 40, object=(9, 0, 9, 8, 26)
	# 	 type=<class 'int'>, size = 14, object=9
	# 	 type=<class 'int'>, size = 12, object=0
	# 	 type=<class 'int'>, size = 14, object=9
	# 	 type=<class 'int'>, size = 14, object=8
	# 	 type=<class 'int'>, size = 14, object=26
	#  type=<class 'tuple'>, size = 40, object=(7, 6, 5, 4, 22)
	# 	 type=<class 'int'>, size = 14, object=7
	# 	 type=<class 'int'>, size = 14, object=6
	# 	 type=<class 'int'>, size = 14, object=5
	# 	 type=<class 'int'>, size = 14, object=4
	# 	 type=<class 'int'>, size = 14, object=22
