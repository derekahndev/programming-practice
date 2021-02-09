def dfs(tree, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in tree[node]:
            parent[i].append(node)
            stack.append(i)
            tree[i].remove(node)
    return parent


n = int(input())
parent = [[] for _ in range(n + 1)]
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

for i in list(dfs(tree, 1, parent))[2:]:
    print(i[0])
