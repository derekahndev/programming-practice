import sys
sys.setrecursionlimit(10**6)


def dfs(graph, v):
    global status

    if not graph[v]:
        if status[v][0] == 'S':
            return status[v][1]
        else:
            return 0

    count = 0

    for i in graph[v]:
        count += dfs(graph, i)

    if status[v][0] == 'W':
        count -= status[v][1]
        if count < 0:
            count = 0
    else:
        count += status[v][1]
    return count


n = int(sys.stdin.readline().strip())
status = [[0, 0] for _ in range(n + 1)]
tree = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    t, a, p = sys.stdin.readline().strip().split()
    status[i][0], status[i][1] = t, int(a)
    tree[int(p)].append(i)

print(dfs(tree, 1))
