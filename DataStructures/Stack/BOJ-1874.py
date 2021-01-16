n = int(input())
check = True
count = 0
result = ''
s = []

for _ in range(n):
    num = int(input())

    while num > count:
        count += 1
        s.append(count)
        result += '+'

    if s[-1] == num:
        s.pop()
        result += '-'
    else:
        check = False
        break

if check:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")
