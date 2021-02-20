import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    global temp
    visited[i][j] = True
    temp += 1
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


m, n, k = map(int, sys.stdin.readline().rstrip().split())
graph = [[1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    ax, ay, bx, by = map(int, sys.stdin.readline().rstrip().split())
    for i in range(ax, bx):
        for j in range(ay, by):
            graph[i][j] = 0

result = []

for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            temp = 0
            dfs(i, j)
            result.append(temp)

result.sort()

print(len(result))

for i in result:
    print(i, end=' ')
