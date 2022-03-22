# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

params = ['name', 'profit']
New_Factory = namedtuple('New_Factory', params)

number_factory = int(input('Введите колтчество предприятий: '))

factories = []
avg_profit = 0

for n in range(1, number_factory + 1):
    factories.append(New_Factory(input(f'Введите название предприятия {n}: '),
                                 int(input(f'введите прибыль предприятия {n}: '))))

    avg_profit += factories[-1].profit


avg_profit /= number_factory
factories_bigger = []
factories_less = []

for item in factories:
    if item.profit > avg_profit:
        factories_bigger.append(item)
    else:
        factories_less.append(item)

print(f'список предприятий: {factories}')
print(f'средний доход: {avg_profit}')
print(f'предприятиия с доходом выше среднего: {factories_bigger}')
print(f'предприятия с доходом ниже среднего: {factories_less}')

