from collections import deque
from sys import stdin


def bfs(a, b):
    queue = deque()
    queue.append([a, 0])
    visited = [False] * 10001
    visited[a] = True
    while queue:
        num, count = queue.popleft()
        if num == b:
            return count
        if num < 1000:
            continue
        for digit in [1, 10, 100, 1000]:
            n = num - num % (digit * 10) // digit * digit
            for _ in range(10):
                if not visited[n] and prime[n]:
                    visited[n] = True
                    queue.append([n, count + 1])
                n += digit


prime = [True] * 10001
for i in range(2, 101):
    if prime[i]:
        j = i * 2
        while j < 10001:
            prime[j] = False
            j += i

t = int(stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, stdin.readline().rstrip().split())
    result = bfs(a, b)
    if result is None:
        print("Impossible")
    else:
        print(result)
