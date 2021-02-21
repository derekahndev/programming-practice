import sys
sys.setrecursionlimit(10**6)


def dfs(x, y, first):
    global check
    if not first:
        visited[x] = True
        if x == y:
            check = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i, y, False)


n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
visited = [False] * n

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if data[j]:
            graph[i].append(j)

for i in range(n):
    for j in range(n):
        check = False
        visited = [False] * n
        dfs(i, j, True)
        if check:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
