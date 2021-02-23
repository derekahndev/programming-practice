import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    global check, count, visited
    visited[v] = True
    ns = students[v - 1]
    if not visited[ns]:
        dfs(ns)
    else:
        if not check[ns]:
            temp = ns
            while temp != v:
                count += 1
                temp = students[temp - 1]
            count += 1
    check[v] = True


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    students = list(map(int, sys.stdin.readline().rstrip().split()))
    check = [False] * (n + 1)
    visited = [False] * (n + 1)

    count = 0
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - count)
