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

'''

допустим вершина 0. (start = 0)
шаг 1:

0-0 = 0
0-1 = 0
0-2 = 1
0-3 = 1
0-4 = 9
0-5 = 0
0-6 = 0
0-7 = 0

путь равен значение в узле + прошлый путь

'''


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
    p = str(start)
    is_min_founded = False
    # parent[start] = start

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
                while index > 0:
                    prev_node = parent[index]
                    p = f'{str(prev_node)} - ' + p
                    index = prev_node
                path[i] = p

        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, path


s = int(input('От какой вершины идти: '))
result = deikstra(g, s)
print('Node : Cost : Path')
print('-' * 30)
for i, node in enumerate(result[0]):
    print(f'{i: 4} : {result[0][i] : 4} : {result[1][i]}')

# print(deikstra(g, 0))
