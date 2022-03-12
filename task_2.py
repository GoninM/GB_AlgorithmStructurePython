# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Введите число: '))

odd = []
even = []

while True:
    if number == 0:
        break

    number_to_check = number % 10
    if number_to_check % 2 == 0:
        even.append(number_to_check)
    else:
        odd.append(number_to_check)

    number //= 10

print(f'четные: {even}')
print(f'нечетные: {odd}')
