# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

numbers = input('введите последовательность чисел через пробел: ').split()

# Variant 1
max_sum = 0
max_n = 0

for num in numbers:
    n = int(num)
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10

    if sum >= max_sum:
        max_sum = sum
        max_n = int(num)

print(f'n = {max_n}, сумма = {max_sum}')

# Variant 2 without split
max_sum = 0
max_n = ''
sum = 0


for s in numbers:
    n = int(s)
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10

    if sum >= max_sum:
        max_sum = sum
        max_n = int(num)


print(f'n = {max_n}, сумма = {max_sum}')