# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1()
# или любой другой из модуля hashlib задача считается не решённой.

import hashlib


def find_substrings(input_string: str) -> list:
    assert len(input_string), 'строка не может быть пустой'

    list_of_strings = []
    length = len(input_string)

    for i in range(length):
        for j in range(i+1, length+1):
            string = input_string[i:j]
            if string not in list_of_strings and string != input_string:
                list_of_strings.append(string)

    return list_of_strings


def count_substrings(string: str, sub_strings: list) -> int:
    assert len(string), 'Строка не может быть пустой'
    for _ in sub_strings:
        assert len(_), 'Одна из строк для поиска пустая'

    counter = 0

    len_string = len(string)
    for sub_string in sub_strings:
        len_substring = len(sub_string)
        hash_sub_string = hash(sub_string)

        for i in range(len_string - len_substring + 1):
            s = string[i: i+len_substring]
            hash_to_compare = hash(s)
            if hash_to_compare == hash_sub_string:
                counter += 1

    return counter


test_string = 'Hello'
test_string_2 = 'OoHOHlo'


print(f'Тестовая строка: "{test_string}" \n')
strings = find_substrings(test_string)

print(f'подстроки (в кол-ве {len(strings)}): ')
print(f'{strings} \n')

print(f'количество различных подстрок: {count_substrings(test_string, strings)}')
