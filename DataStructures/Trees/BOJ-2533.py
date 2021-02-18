import sys
sys.setrecursionlimit(10**6)


def dfs(cur):
    visited[cur] = True
    dp[cur][0] = 0
    dp[cur][1] = 1
    for i in tree[cur]:
        if not visited[i]:
            dfs(i)
            dp[cur][0] += max(dp[i][0], dp[i][1])
            dp[cur][1] += dp[i][0]


n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().strip().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)

dfs(1)

print(n - max(dp[1][0], dp[1][1]))
