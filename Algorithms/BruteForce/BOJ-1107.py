from sys import stdin

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

broken = [False] * 10

for _ in range(m):
    data = list(map(int, stdin.readline().rstrip().split()))
    for i in data:
        broken[i] = True

result = abs(n - 100)

for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if broken[int(num[i])]:
            break
        elif i == len(num) - 1:
            result = min(result, abs(n - int(num)) + len(str(num)))

print(result)
