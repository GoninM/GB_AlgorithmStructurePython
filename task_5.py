# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

i = 1
result_str = ''
for code in range(32, 127 + 1):

    result_str += f'{str(code):3}: {chr(code)}'
    i+=1
    if i>10:
        result_str += f'\n'
        i=1
    else:
        result_str += f'   '

print(result_str)