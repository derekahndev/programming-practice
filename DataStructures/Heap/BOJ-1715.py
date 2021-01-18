import heapq

n = int(input())
heap = []
result = 0

for i in range(n):
    num = int(input())
    heapq.heappush(heap, num)

if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        result += temp1 + temp2
        heapq.heappush(heap, temp1 + temp2)

    print(result)
