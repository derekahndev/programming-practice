def check(word):
    temp = []
    for i in range(len(word)):
        if temp and temp[-1] == word[i]:
            temp.pop()
        else:
            temp.append(word[i])
    if not temp:
        return True
    else:
        return False


n = int(input())
result = 0

for _ in range(n):
    data = input()
    if check(data):
        result += 1

print(result)
