from sys import stdin

n = int(stdin.readline().rstrip())
a_list = []
b_list = []
c_list = []
d_list = []

for _ in range(n):
    a, b, c, d = map(int, stdin.readline().rstrip().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

ab_dict, cd_dict = {}, {}

for a in a_list:
    for b in b_list:
        if ab_dict.get(a + b):
            ab_dict[a + b] += 1
        else:
            ab_dict[a + b] = 1

for c in c_list:
    for d in d_list:
        if cd_dict.get(c + d):
            cd_dict[c + d] += 1
        else:
            cd_dict[c + d] = 1

result = 0

for _, key in enumerate(ab_dict):
    if cd_dict.get(-key):
        result += (ab_dict[key] * cd_dict[-key])

print(result)
