convert_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
result = ''
temp = []

data = input()

for i in range(len(data)):
    if 'A' <= data[i] <= 'Z':
        result += data[i]
    elif data[i] == '(':
        temp.append(data[i])
    elif data[i] == ')':
        while temp and temp[-1] != '(':
            result += temp.pop()
        temp.pop()
    else:
        while temp and convert_dict[data[i]] <= convert_dict[temp[-1]]:
            result += temp.pop()
        temp.append(data[i])

while temp:
    result += temp.pop()

print(result)
