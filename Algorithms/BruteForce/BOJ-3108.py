from collections import deque
from sys import stdin

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                if data[nx][ny] == 1 and not check[nx][ny]:
                    check[nx][ny] = True
                    queue.append([nx, ny])


n = int(stdin.readline().rstrip())
data = [[0] * 2001 for _ in range(2001)]
check = [[False] * 2001 for _ in range(2001)]
start = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
    x1 += 500
    y1 += 500
    x2 += 500
    y2 += 500
    x1 *= 2
    y1 *= 2
    x2 *= 2
    y2 *= 2
    start.append([x1, y1])
    for i in range(x1, x2 + 1):
        if i == x1 or i == x2:
            for j in range(y1, y2 + 1):
                data[i][j] = 1
        else:
            data[i][y1] = 1
            data[i][y2] = 1

result = 0

for i in range(len(start)):
    x, y = start[i]
    if not check[x][y]:
        bfs(x, y)
        result += 1

if data[1000][1000] == 1:
    result -= 1

print(result)
