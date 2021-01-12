from sys import stdin


class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        item = self.list[self.len - 1]
        del self.list[self.len - 1]
        self.len -= 1
        return item

    def size(self):
        return self.len

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        return self.list[-1]


n = int(stdin.readline().strip())
stack = Stack()

for _ in range(n):
    data = stdin.readline().strip().split()
    command = data[0]

    if command == "push":
        stack.push(data[1])
    elif command == "pop":
        print(stack.pop())
    elif command == "size":
        print(stack.size())
    elif command == "empty":
        print(stack.empty())
    elif command == "top":
        print(stack.top())
