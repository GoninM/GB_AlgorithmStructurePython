# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# version 1

number = input('введите число: ')

result = ''

for i in range(1, len(number)+1):
    result += number[-i]

print(f'варианат 1: {result}')


# version2
number = int(number)
result = ''

while True:
    if number == 0:
        break

    result += str(number % 10)

    number //= 10

print(f'варианат 2: {result}')
