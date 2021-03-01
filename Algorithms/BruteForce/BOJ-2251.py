from collections import deque
from sys import stdin


def bfs(a, b, c):
    queue = deque()
    queue.append([0, 0, c])
    while queue:
        x, y, z = queue.popleft()
        if check[x][y]:
            continue
        check[x][y] = True
        if not x:
            result[z] = True
        if x + y > b:
            queue.append([x + y - b, b, z])
        else:
            queue.append([0, x + y, z])
        if x + z > c:
            queue.append([x + z - c, y, c])
        else:
            queue.append([0, y, x + z])
        if y + x > a:
            queue.append([a, y + x - a, z])
        else:
            queue.append([y + x, 0, z])
        if y + z > c:
            queue.append([x, y + z - c, c])
        else:
            queue.append([x, 0, y + z])
        if z + x > a:
            queue.append([a, y, z + x - a])
        else:
            queue.append([z + x, y, 0])
        if z + y > b:
            queue.append([x, b, z + y - b])
        else:
            queue.append([x, z + y, 0])


a, b, c = map(int, stdin.readline().rstrip().split())

check = [[False] * 201 for _ in range(201)]
result = [False] * 201

bfs(a, b, c)

for i in range(201):
    if result[i]:
        print(i, end=' ')
