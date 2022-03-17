import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'test {i} is OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}
    print(f' in: n= {n} {fib_d}')

    def _fib_dict(n):
        print(f'func in n= {n} {fib_d}')

        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n-1) + _fib_dict(n-2)

        print(f'func out {fib_d}')
        return fib_d[n]

    print(f'out {fib_d}')

    return _fib_dict(n)


test_fib(fib_dict)
