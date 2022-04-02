# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

'''
N = 2
  1 2
  ------
1| 0 1
2| 1 0

1 рукопожатие

N = 3
  1 2 3
  ------
1| 0 1 1
2| 1 0 1
3| 1 1 0
3 - рукопожатия

N = 4
  1 2 3 4
  ------
1| 0 1 1 1
2| 1 0 1 1
3| 1 1 0 1
4| 1 1 1 0
6 - рукопожатий

N = 5
  1 2 3 4 5
  -----------
1| 0 1 1 1 1
2| 1 0 1 1 1
3| 1 1 0 1 1
4| 1 1 1 0 1
5| 1 1 1 1 0
10 - рукопожатий

'''


def calc_handshake(graph):
    result = 0

    for i in range(n):
        for j in range(i, n):
            result += graph[i][j]

    return result


n = int(input(f'Введите количество друзей: '))

graph = [[None for i in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = 1

print(f'Граф:')
print(*graph, sep='\n')

print(f'\nколичество рукопожатий = {calc_handshake(graph)}')
