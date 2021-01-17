from collections import deque

num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    idx = deque([x for x in range(n)])

    order = 0

    while queue:
        if queue[0] == max(queue):
            order += 1
            if idx[0] == m:
                print(order)
                break
            else:
                queue.popleft()
                idx.popleft()
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())
