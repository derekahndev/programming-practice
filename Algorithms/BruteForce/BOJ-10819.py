from itertools import permutations

n = int(input())
data = permutations(list(map(int, input().split(' '))))
result = 0

for d in data:
    temp = 0
    for i in range(n - 1):
        temp += abs(d[i] - d[i + 1])
    result = max(result, temp)

print(result)
