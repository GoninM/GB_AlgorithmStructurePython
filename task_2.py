# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import deque


class HexNumber:
    __DICT_HEX_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    __DICT_INT_TO_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                         10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def __init__(self, number: str):
        self.__number = deque(number)

    def __add__(self, other):
        len_1 = len(self.__number)
        len_2 = len(other.__number)

        if len_1 > len_2:
            max = self.__number
            min = other.__number
            max_rank = len_1
            min_rank = len_2
        else:
            max = other.__number
            min = self.__number
            max_rank = len_2
            min_rank = len_1

        result = deque()
        carry = 0

        for i in range(1, max_rank+1):
            if i <= min_rank:
                current_sum = self.__DICT_HEX_TO_INT[max[max_rank - i]] + \
                              other.__DICT_HEX_TO_INT[min[min_rank - i]] + \
                              carry
            else:
                current_sum = self.__DICT_HEX_TO_INT[max[max_rank - i]] + carry

            if current_sum >= 16:
                carry = 1
                current_sum -= 16
            else:
                carry = 0

            result.appendleft(self.__DICT_INT_TO_HEX[current_sum])

            if i == max_rank and carry == 1:
                result.appendleft(self.__DICT_INT_TO_HEX[carry])

        return HexNumber(result)

    def __mul__(self, other):
        len_1 = len(self.__number)
        len_2 = len(other.__number)

        result = HexNumber(deque('0'))

        for indx_1 in range(1, len_1 + 1):
            num = deque()
            carry = 0
            for indx_2 in range(1, len_2 + 1):
                current_mul = (other.__DICT_HEX_TO_INT[other.__number[len_2 - indx_2]]) * \
                               self.__DICT_HEX_TO_INT[self.__number[len_1 - indx_1]] + carry

                if current_mul >= 16:
                    carry = current_mul // 16
                    current_mul %= 16
                else:
                    carry = 0

                num.appendleft(self.__DICT_INT_TO_HEX[current_mul])

                if indx_2 == len_2 and carry != 0:
                    num.appendleft(self.__DICT_INT_TO_HEX[carry])

            for _ in range(indx_1-1):
                num.append(self.__DICT_INT_TO_HEX[0])

            result = result + HexNumber(num)

        return result

    def __str__(self):
        res = '0x'
        for s in self.__number:
            res += s
        return res


num_1 = HexNumber(input(f'введите 1-ое шестнадцатиричное число: ').upper())
num_2 = HexNumber(input(f'введите 2-ое шестнадцатиричное число: ').upper())

print(f'{num_1} + {num_2} = {num_1 + num_2}')
print(f'{num_1} * {num_2} = {num_1 * num_2}')







