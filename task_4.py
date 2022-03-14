# 4. Определить, какое число в массиве встречается чаще всего.
import random

test_data = [random.randint(-10, 10) for _ in range(10)]
print(test_data)

result = {}
max_value = 0
max_count = 0

for item in test_data:
    if item in result:
        result[item] += 1
    else:
        result[item] = 1

    if result[item] >= max_count:
        max_value = item
        max_count = result[item]


# print(result)
print(f'число {max_value} встречается в массиве {max_count} раз')


