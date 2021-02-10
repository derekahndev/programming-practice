from sys import stdin


def dfs_edge(graph, v, passed):
    cnt = len(graph[v])
    passed[v] = True
    for i in graph[v]:
        if not passed[i]:
            cnt += dfs_edge(graph, i, passed)
    return cnt


def dfs_vertex(graph, v, visited):
    cnt = 1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += dfs_vertex(graph, i, visited)
    return cnt


count = 1

while True:
    n, m = map(int, stdin.readline().strip().split())
    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n + 1)]
    passed = [False] * (n + 1)
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, stdin.readline().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    result = 0

    for i in range(1, n + 1):
        if visited[i] is False:
            edge = dfs_edge(tree, i, passed)
            vertex = dfs_vertex(tree, i, visited)
            if edge / 2 == vertex - 1:
                result += 1

    print("Case {}: ".format(count), end='')

    if result == 0:
        print("No trees.")
    elif result == 1:
        print("There is one tree.")
    else:
        print("A forest of", result, "trees.")

    count += 1
