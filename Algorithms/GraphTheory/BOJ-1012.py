import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    visited[i][j] = True
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y][x] = 1

    result = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)
