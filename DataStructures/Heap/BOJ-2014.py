import heapq

k, n = map(int, input().split())
data = list(map(int, input().split()))
heap = []

for d in data:
    heapq.heappush(heap, d)

for _ in range(n):
    num = heapq.heappop(heap)
    for i in range(k):
        temp = num * data[i]
        heapq.heappush(heap, temp)

        if num % data[i] == 0:
            break

print(num)
