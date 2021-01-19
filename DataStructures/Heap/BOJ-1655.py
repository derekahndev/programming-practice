from sys import stdin
import heapq

n = int(stdin.readline().rstrip())

left, right = [], []

for _ in range(n):
    num = int(stdin.readline().rstrip())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        left_temp = -heapq.heappop(left)
        right_temp = heapq.heappop(right)
        heapq.heappush(right, left_temp)
        heapq.heappush(left, -right_temp)

    print(-left[0])
