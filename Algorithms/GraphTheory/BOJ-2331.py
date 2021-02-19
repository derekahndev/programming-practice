import sys
sys.setrecursionlimit(10**6)


def next(a, p):
    data = str(a)
    result = 0
    for i in data:
        result += pow(int(i), p)
    return result


def dfs(a, p, check, count):
    if check[a] != 0:
        return check[a] - 1
    check[a] = count
    temp = next(a, p)
    return dfs(temp, p, check, count + 1)


a, p = map(int, input().split())
check = [0] * 250000

print(dfs(a, p, check, 1))
