# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random


def make_graph(n):
    g = {_: [] for _ in range(n)}

    for i in range(len(g)):
        nums = list(range(n))
        nums.remove(i)
        # print(nums)
        g[i] = [random.choice(nums) for _ in range(random.choice(range(n)))]

    # for k, v in g.items():
    #     print(f'{k} : {v}')

    return g


def deep_search(graf, start, is_visited, res):
    is_visited[start] = True

    for g in graf[start]:
        if not is_visited[g]:
            res.append(g)
            deep_search(graf, g, is_visited, result)


test_graf = {
    0: [1, 3, 4],
    1: [2, 5],
    2: [1, 6],
    3: [1, 5, 7],
    4: [2, 6],
    5: [6],
    6: [5],
    7: [6]
}

is_marked = [False] * (len(test_graf))

for i in range(len(test_graf)):
    is_marked = [False] * (len(test_graf))
    result = []
    deep_search(test_graf, i, is_marked, result)
    print(f'вершина {i} путь: {result}')


st = random.randint(7, 20)
print(f'количество вершин: {st}')

test_graf_2 = make_graph(st)
print(f'Граф тестовый:')
for k, v in test_graf_2.items():
    print(f'{k} : {v}')

for i in range(st):
    is_marked = [False] * st
    result = []
    deep_search(test_graf_2, i, is_marked, result)
    print(f'вершина {i} путь: {result}')
