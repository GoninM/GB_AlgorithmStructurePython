# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# за 10 попыток число не отгадано, вывести ответ.

import random

guess_number = 10
number = random.randint(0, 100)
# print(number)

while guess_number != 0:
    n = int(input('Угадай число: '))
    if n > number:
        print('не угадал. загадонное число меньше')
    elif n < number:
        print('не угадал. загадонное число больше')
    else:
        print('Угадал!')
        break

    guess_number -= 1

print('попытки закончились:(')