from sys import stdin

n = int(stdin.readline().rstrip())
queue = []

for _ in range(n):
    data = stdin.readline().rstrip().split()
    command = data[0]

    if command == "push":
        queue.insert(0, data[1])
    elif command == "pop":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command == "front":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[0])
        else:
            print(-1)
