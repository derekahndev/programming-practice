import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    global temp
    visited[i][j] = True
    temp += 1
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx <= n) and (0 <= ny <= m):
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


m, n, k = map(int, sys.stdin.readline().rstrip().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[False] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[y][x] = 1

result = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] and not visited[i][j]:
            temp = 0
            dfs(i, j)
            result = max(result, temp)

print(result)
