n = int(input())
idx = (-1, -1)
length = 0
temp = []

for _ in range(n):
    l, h = map(int, input().split())
    if h > idx[1]:
        idx = (l, h)
    length = max(length, l)
    temp.append((l, h))

data = [0] * (length + 1)

for l, h in temp:
    data[l] = h

high = data[0]
result = 0

for i in range(idx[0] + 1):
    if data[i] > high:
        high = data[i]
    result += high

high = data[-1]

for i in range(length, idx[0], -1):
    if data[i] > high:
        high = data[i]
    result += high

print(result)
