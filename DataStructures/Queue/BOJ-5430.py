from collections import deque

num = int(input())

for _ in range(num):
    asc = True
    err = False
    p = input()
    n = int(input())
    data = input()
    data = deque(data[1:-1].split(','))

    if n == 0:
        data = deque([])

    for i in range(len(p)):
        if p[i] == 'R':
            asc = not asc
        elif p[i] == 'D':
            if not data:
                err = True
                break
            else:
                if asc:
                    data.popleft()
                else:
                    data.pop()

    if err:
        print("error")
    else:
        if not asc:
            data.reverse()
        print('[', end='')
        print(','.join(data), end='')
        print(']')
