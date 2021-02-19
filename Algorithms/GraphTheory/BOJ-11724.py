from sys import stdin
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        val = queue.popleft()
        for i in graph[val]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)
