import heapq

n = int(input())
heap = []

data = map(int, input().split())
for d in data:
    heapq.heappush(heap, d)

answer = heap[0]

for _ in range(n - 1):
    data = map(int, input().split())
    for d in data:
        if d > answer:
            heapq.heappush(heap, d)
            heapq.heappop(heap)
            answer = heap[0]

print(answer)
