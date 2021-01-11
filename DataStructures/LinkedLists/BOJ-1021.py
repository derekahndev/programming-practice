def left_move(i, data):
    move = 0
    while data[0] != i:
        temp = data.pop(0)
        data.append(temp)
        move += 1
    return move


def right_move(i, data):
    move = 0
    while data[0] != i:
        temp = data.pop()
        data.insert(0, temp)
        move += 1
    return move


n, m = map(int, input().split())
index = list(map(int, input().split()))
result = 0

data = [x for x in range(1, n + 1)]

for i in index:
    idx = data.index(i)
    if idx > (len(data) // 2):
        result += right_move(i, data)
        data.pop(0)
    else:
        result += left_move(i, data)
        data.pop(0)

print(result)
