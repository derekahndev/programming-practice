import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    visited[i][j] = True
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)
