from sys import stdin


def key_logger(data):
    stack1 = []
    stack2 = []

    for i in range(len(data)):
        if data[i] == '<':
            if stack1:
                stack2.append(stack1.pop())
            else:
                continue
        elif data[i] == '>':
            if stack2:
                stack1.append(stack2.pop())
            else:
                continue
        elif data[i] == '-':
            if stack1:
                stack1.pop()
            else:
                continue
        else:
            stack1.append(data[i])

    print(''.join(stack1 + list(reversed(stack2))))


n = int(input())

for _ in range(n):
    data = list(stdin.readline().strip())
    key_logger(data)
