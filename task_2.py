# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def deikstra(graf, start):

    length = len(graf)
    is_visited = [False] * length
    is_path_changed = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    path = ['no way' for _ in range(length)]
    p = [-10] * length

    cost[start] = 0
    p[start] = 0
    path[start] = str(start)
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, node in enumerate(graf[start]):

            if node != 0 and not is_visited[i]:
                if cost[i] > node + cost[start]:
                    cost[i] = node + cost[start]
                    is_path_changed[i] = True
                    parent[i] = start

        for i in range(length):
            if is_path_changed[i]:
                is_path_changed[i] = False
                index = i
                p = str(i)
                # print(p)
                while index > 0:
                    # print(f'parent[{index}] = {parent[index]}')
                    prev_node = parent[index]
                    if prev_node != -1:
                        p = f'{str(prev_node)} -> ' + p
                    index = prev_node
                path[i] = p
                # print(f'path[{i}] = {path[i]}')
        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, path


# s = int(input('От какой вершины идти: '))

for s in range(len(g)):
    result = deikstra(g, s)
    print('-' * 15, f'вершина {s}', '-' * 15)
    # print('-' * 15 )

    for i, node in enumerate(result[0]):
        # if i != s:
        print(f'минимальное расстояние от вершиниы {s: 3} до вершины {i: 3} равно {result[0][i] : 4} и проходит через вершины: {result[1][i]}')
