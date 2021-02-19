from collections import deque
from sys import stdin


def bfs(start):
    queue = deque([start])
    color[start] = 1
    while queue:
        val = queue.popleft()
        for i in graph[val]:
            if color[i] == 0:
                color[i] = -1 * color[val]
                queue.append(i)
            elif color[i] == color[val]:
                return False
    return True


k = int(stdin.readline().rstrip())

for _ in range(k):
    v, e = map(int, stdin.readline().rstrip().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = True

    for i in range(1, v + 1):
        if color[i] == 0:
            answer = bfs(i)
            if not answer:
                break

    if answer:
        print("YES")
    else:
        print("NO")
