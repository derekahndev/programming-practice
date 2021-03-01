from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
data = []

for _ in range(n):
    data.append(list(map(int, stdin.readline().rstrip())))

result = 0

for i in range(1, m - 1):
    for j in range(i + 1, m):
        s1 = sum([data[a][b] for a in range(n) for b in range(i)])
        s2 = sum([data[a][b] for a in range(n) for b in range(i, j)])
        s3 = sum([data[a][b] for a in range(n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

for i in range(1, n - 1):
    for j in range(i + 1, n):
        s1 = sum([data[a][b] for a in range(i) for b in range(m)])
        s2 = sum([data[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([data[a][b] for a in range(j, n) for b in range(m)])
        result = max(result, s1 * s2 * s3)

for i in range(1, n):
    for j in range(1, m):
        s1 = sum([data[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([data[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([data[a][b] for a in range(n) for b in range(j)])
        result = max(result, s1 * s2 * s3)

for i in range(1, n):
    for j in range(1, m):
        s1 = sum([data[a][b] for a in range(i) for b in range(j)])
        s2 = sum([data[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([data[a][b] for a in range(n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

for i in range(1, n):
    for j in range(1, m):
        s1 = sum([data[a][b] for a in range(i) for b in range(m)])
        s2 = sum([data[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([data[a][b] for a in range(i, n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

for i in range(1, m):
    for j in range(1, n):
        s1 = sum([data[a][b] for a in range(j) for b in range(i)])
        s2 = sum([data[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([data[a][b] for a in range(j, n) for b in range(m)])
        result = max(result, s1 * s2 * s3)

print(result)
