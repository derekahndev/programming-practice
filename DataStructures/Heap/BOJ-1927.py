from sys import stdin
import heapq

n = int(stdin.readline().rstrip())
heap = []

for i in range(n):
    num = int(stdin.readline().rstrip())
    if num:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
