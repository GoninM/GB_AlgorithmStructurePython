# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

import cProfile


def test(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, item in enumerate(lst):
        assert item == func(i+1)
        print(f'Test passed. element №{i+1} is {lst[i]}')


def erastofens_sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = 2 * i

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]

    return result


def erastofen(n):
    result = [2]

    if n <= len(result):
        return result[n-1]
    else:
        number_to_check = result[-1] + 10000
        while len(result) < n:
            sieve = [i for i in range(number_to_check)]
            sieve[1] = 0

            for i in range(2, number_to_check):
                if sieve[i] != 0:
                    j = 2 * i

                    while j < number_to_check:
                        sieve[j] = 0
                        j += i

            result = [i for i in sieve if i != 0]

    return result[n-1]


def simple(n):
    result = [2]

    if n <= len(result):
        return result[n-1]
    else:
        number_to_check = result[-1] + 1
        index = 0

        while len(result) < n:
            if number_to_check % result[index] == 0 and index < len(result) - 1:
                number_to_check += 1
                index = 0
            else:
                index += 1

                if index >= len(result):
                    result.append(number_to_check)
                    number_to_check += 1
                    index = 0

        return result[n-1]

# print(erastofens_sieve(100))

# print(f'simple')
# test(simple)
# "task_2.simple(10)"
# 1000 loops, best of 5: 22 usec per loop

# "task_2.simple(100)"
# 1000 loops, best of 5: 1.47 msec per loop

# "task_2.simple(500)"
# 1000 loops, best of 5: 46 msec per loop


# print(f'erastofen')
# test(erastofen)

# task_2.erastofen(10)
# 1000 loops, best of 5: 442 usec per loop

# task_2.erastofen(100)
# 1000 loops, best of 5: 403 usec per loop

# task_2.erastofen(500)
# 1000 loops, best of 5: 4.94 msec per loop

# cProfile.run("simple(10)")
#  153 function calls in 0.000 seconds
# ncalls tottime percall cumtime  percall filename: lineno(function)
# 1 0.000 0.000  0.000 0.000 < string >: 1( < module >)
# 1 0.000 0.000 0.000 0.000 task_2.py: 69(simple)
# 1 0.000 0.000 0.000 0.000 {built - in method builtins.exec}
# 140 0.000 0.000 0.000 0.000 {built - in method builtins.len}
# 9 0.000 0.000 0.000 0.000 {method 'append' of 'list' objects}
# 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("simple(100)")
# 11595 function calls in 0.004 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.004    0.004 <string>:1(<module>)
# 1    0.003    0.003    0.004    0.004 task_2.py:69(simple)
# 1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
# 11492    0.001    0.000    0.001    0.000 {built-in method builtins.len}
# 99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("simple(500)")
# 263597 function calls in 0.140 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.140    0.140 <string>:1(<module>)
# 1    0.104    0.104    0.140    0.140 task_2.py:69(simple)
# 1    0.000    0.000    0.140    0.140 {built-in method builtins.exec}
# 263094    0.036    0.000    0.036    0.000 {built-in method builtins.len}
# 499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("erastofen(10)")
# 9 function calls in 0.005 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.005    0.005 <string>:1(<module>)
# 1    0.004    0.004    0.005    0.005 task_2.py:45(erastofen)
# 1    0.000    0.000    0.000    0.000 task_2.py:53(<listcomp>)
# 1    0.001    0.001    0.001    0.001 task_2.py:64(<listcomp>)
# 1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
# 3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("erastofen(100)")
# 9 function calls in 0.005 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.005    0.005 <string>:1(<module>)
# 1    0.004    0.004    0.004    0.004 task_2.py:45(erastofen)
# 1    0.000    0.000    0.000    0.000 task_2.py:53(<listcomp>)
# 1    0.000    0.000    0.000    0.000 task_2.py:64(<listcomp>)
# 1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
# 3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("erastofen(500)")
# 9 function calls in 0.004 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.004    0.004 <string>:1(<module>)
# 1    0.003    0.003    0.004    0.004 task_2.py:45(erastofen)
# 1    0.000    0.000    0.000    0.000 task_2.py:53(<listcomp>)
# 1    0.000    0.000    0.000    0.000 task_2.py:64(<listcomp>)
# 1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
# 3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

