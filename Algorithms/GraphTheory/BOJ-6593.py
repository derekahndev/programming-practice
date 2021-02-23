from collections import deque
import sys


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])
    distance[x][y][z] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if graph[nx][ny][nz] == 'E':
                    print("Escaped in {} minute(s).".format(distance[x][y][z]))
                    return
                if graph[nx][ny][nz] == '.' and distance[nx][ny][nz] == 0:
                    distance[nx][ny][nz] = distance[x][y][z] + 1
                    queue.append([nx, ny, nz])
    print("Trapped!")


while True:
    l, r, c = map(int, sys.stdin.readline().rstrip().split())
    if l == 0 and r == 0 and c == 0:
        break

    graph = [[[] * c for _ in range(r)] for _ in range(l)]
    distance = [[[0] * c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        graph[i] = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    bfs(i, j, k)
