def dfs(root):
    global count
    leaf = True
    visited[root] = 1
    for i in range(n):
        if tree[root][i] == 1 and visited[i] == 0:
            leaf = False
            dfs(i)
    if leaf:
        count += 1


n = int(input())
data = list(map(int, input().split()))
delete = int(input())
tree = [[0] * n for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(len(data)):
    if data[i] != -1:
        tree[i][data[i]] = 1
        tree[data[i]][i] = 1
    else:
        root = i

for i in range(n):
    tree[i][delete] = 0
    tree[delete][i] = 0

count = 0

dfs(root)

if delete == root:
    print(0)
else:
    print(count)
