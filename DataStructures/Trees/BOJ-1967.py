import sys
sys.setrecursionlimit(10**6)


def dfs(start, graph, result):
    for children, weight in tree[start]:
        if result[children] == 0:
            result[children] = result[start] + weight
            dfs(children, graph, result)


n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, children, weight = map(int, sys.stdin.readline().strip().split())
    tree[parent].append([children, weight])
    tree[children].append([parent, weight])

result1 = [0 for _ in range(n + 1)]

dfs(1, tree, result1)
result1[1] = 0

index = 0
max_weight = 0

for i in range(len(result1)):
    if max_weight < result1[i]:
        index = i
        max_weight = result1[i]

result2 = [0 for _ in range(n + 1)]

dfs(index, tree, result2)
result2[index] = 0

print(max(result2))
