from collections import deque
import sys
sys.setrecursionlimit(10**6)


def bfs():
    queue = deque()
    queue.append([0, 0])
    while queue:
        a, b = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx = a + dx
            ny = b + dy
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = graph[a][b] + 1


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]

for i in range(n):
    data = sys.stdin.readline().rstrip()
    for j in range(m):
        graph[i].append(int(data[j]))

bfs()
print(graph[n - 1][m - 1])
