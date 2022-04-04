# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def make_graph(n):
    g = {i: [] for i in range(n)}

    for i in range(len(g)):
        for j in range(len(g)):
            if j != i:
                g[i].append(j)

    for k, v in g.items():
        print(f'{k} : {v}')

    return g


def make_graph_2(n):
    g = {i: [] for i in range(n)}

    i = 0
    while i < n:
        j = 0
        while j < n:
            if j == i and j != n-1:
                j += 1
            else:
                break

            node = input(f'Введите {j} вершину для вершины {i}. для остановки пустая строка: ')
            if not node:
                break
            elif int(node) == i:
                print(f'номера вершин не должны совпадать')
            else:
                g[i].append(int(node))
                j += 1

        i += 1

    for k, v in g.items():
        print(f'{k} : {v}')

    return g


def deep_search(graf):
    pass

n = int(input('введите кол-во узлов: '))
make_graph_2(n)

