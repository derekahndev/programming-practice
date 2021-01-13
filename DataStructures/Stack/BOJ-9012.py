def test(data):
    temp = []
    for i in range(len(data)):
        if data[i] == '(':
            temp.append(data[i])
        else:
            if not temp:
                return False
            temp.pop()
    if temp:
        return False
    return True


t = int(input())

for _ in range(t):
    data = input()
    if test(data):
        print("YES")
    else:
        print("NO")
