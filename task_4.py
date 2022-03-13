# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('введите колво элементов ряда: '))

b0 = 1
q = -0.5

# вариант 1. цикл
result = 0
bn = b0
for i in range(n):
    print(f"b{i} = {bn}")
    result += bn
    bn *= q

print(f'вариант 1. сумма = {result}')


# вариант 2. формула суммы геометирческой прогрессии
result = b0 * (1 - q ** n) / (1 - q)
print(f'вариант 2. сумма = {result}')
