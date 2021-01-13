n = int(input())
data = input()

alphabet = [0] * n
for i in range(n):
    alphabet[i] = int(input())

result = []

for i in range(len(data)):
    if 'A' <= data[i] <= 'Z':
        result.append(alphabet[ord(data[i]) - ord('A')])
    else:
        num2 = result.pop()
        num1 = result.pop()
        if data[i] == '+':
            result.append(num1 + num2)
        elif data[i] == '-':
            result.append(num1 - num2)
        elif data[i] == '*':
            result.append(num1 * num2)
        elif data[i] == '/':
            result.append(num1 / num2)

print('%.2f' % result[0])
