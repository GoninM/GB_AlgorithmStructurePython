# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('введите год: '))

result = ''
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            result = 'високосный'
        else:
            result = 'невисокосный'
    else:
        result = 'високосный'
else:
    result = 'невисокосный'

print(f'год {result}')

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ('високосный')
else:
    print('невисокосный')