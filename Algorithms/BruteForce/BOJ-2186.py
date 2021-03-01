import sys
sys.setrecursionlimit(10**6)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, idx):
    if idx == len(word):
        return 1
    if c[x][y][idx] != -1:
        return c[x][y][idx]
    c[x][y][idx] = 0
    for i in range(4):
        temp_x, temp_y = x, y
        for _ in range(k):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if data[nx][ny] == word[idx]:
                    c[x][y][idx] += dfs(nx, ny, idx + 1)
                temp_x, temp_y = nx, ny
    return c[x][y][idx]


n, m, k = map(int, sys.stdin.readline().rstrip().split())
data = []
start = []

for _ in range(n):
    data.append(list(sys.stdin.readline().rstrip()))

word = list(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(m):
        if data[i][j] == word[0]:
            start.append([i, j])

result = 0
c = [[[-1] * len(word) for _ in range(m)] for _ in range(n)]

for i in range(len(start)):
    x, y = start[i]
    result += dfs(x, y, 1)

print(result)
