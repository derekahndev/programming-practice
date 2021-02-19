import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    data = [0] + list(map(int, sys.stdin.readline().strip().split()))
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        graph[i].append(data[i])
        graph[data[i]].append(i)

    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            result += 1

    print(result)
