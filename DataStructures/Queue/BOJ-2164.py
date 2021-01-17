from collections import deque

n = int(input())
queue = deque([(x + 1) for x in range(n)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
