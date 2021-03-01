from itertools import permutations
from sys import stdin


def route(p):
    global n, data
    temp = 0

    for i in range(n - 1):
        if data[p[i]][p[i + 1]] != 0:
            temp += data[p[i]][p[i + 1]]
        else:
            return -1

    if data[p[-1]][p[0]] != 0:
        temp += data[p[-1]][p[0]]
    else:
        return -1

    return temp


n = int(stdin.readline().rstrip())
data = []

for _ in range(n):
    data.append(list(map(int, stdin.readline().rstrip().split())))

perm_lists = permutations([x for x in range(n)])
result = int(1e9)

for perm in perm_lists:
    perm_result = route(perm)
    if perm_result != -1:
        result = min(result, perm_result)

print(result)
