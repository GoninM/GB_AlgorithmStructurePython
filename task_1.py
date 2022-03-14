# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

result = [0 for _ in range(8)]

for num in range(2, 100):
    for dev in range(2, 10):
        if num % dev == 0:
            result[dev-2] += 1

print('В диапазоне натуральных чисел от 2 до 99')
for item in result:
    print(f'кратно {result.index(item) + 2} - {item} значений')
