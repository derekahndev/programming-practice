n, k = map(int, input().split())
idx = 0
result = []

data = [x for x in range(1, n + 1)]

while data:
    idx = (idx + (k - 1)) % len(data)
    temp = data.pop(idx)
    result.append(temp)

print('<' + str(result)[1:-1] + '>')
