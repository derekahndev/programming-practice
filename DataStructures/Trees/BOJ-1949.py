import sys
sys.setrecursionlimit(10**6)


def dfs(cur):
    visited[cur] = True
    for i in tree[cur]:
        if not visited[i]:
            dfs(i)
            dp[cur][0] += max(dp[i][0], dp[i][1])
            dp[cur][1] += dp[i][0]


n = int(sys.stdin.readline().strip())
cost = [0] + list(map(int, sys.stdin.readline().strip().split()))
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, cost[i]] * 2 for i in range(n + 1)]
visited = [False] * (n + 1)

dfs(1)

print(max(dp[1][0], dp[1][1]))
