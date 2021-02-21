from collections import deque
import sys


def bfs(start):
    queue = deque([start])
    result = 0
    while queue:
        v = queue.popleft()
        for i in range(len(graph[v])):
            if graph[v][i] != 0 and not visited[v][i]:
                queue.append(graph[v][i])
                visited[v][i] = 1
                result += 1
                break
            if visited[v][i]:
                return -1
    return result


n, m, p = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(m + 1)]
visited = [[] for _ in range(m + 1)]

for _ in range(n):
    favorite, hate = map(int, sys.stdin.readline().rstrip().split())
    graph[hate].append(favorite)
    visited[hate].append(0)

print(bfs(p))
