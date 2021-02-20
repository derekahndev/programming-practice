import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    global temp
    visited[i][j] = True
    temp += 1
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        nx = i + dx
        ny = j + dy
        if (0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


n = int(sys.stdin.readline().rstrip())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    data = sys.stdin.readline().rstrip()
    for j in range(len(data)):
        graph[j][i] = int(data[j])

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            temp = 0
            dfs(i, j)
            result.append(temp)

result.sort()

print(len(result))

for i in result:
    print(i)
