import sys
sys.setrecursionlimit(10**6)


def dfs(i, j, limit):
    visited[i][j] = True
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] >= limit and not visited[nx][ny]:
                dfs(nx, ny, limit)


n = int(sys.stdin.readline().rstrip())
graph = []
visited = [[False] * n for _ in range(n)]

max_value = 0

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    max_value = max(max_value, max(data))
    graph.append(data)

result = 0

for i in range(1, max_value + 1):
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] >= i and not visited[j][k]:
                dfs(j, k, i)
                temp += 1
    result = max(result, temp)

print(result)
