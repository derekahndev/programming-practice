import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    visited[i][j] = True
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] == graph[i][j] and not visited[nx][ny]:
                dfs(nx, ny)


n = int(sys.stdin.readline().rstrip())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    data = sys.stdin.readline().rstrip()
    for j in range(len(data)):
        graph[j][i] = data[j]

result = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result += 1

print(result)

result = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result += 1

print(result)
