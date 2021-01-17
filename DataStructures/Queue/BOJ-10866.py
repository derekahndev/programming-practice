from sys import stdin

n = int(stdin.readline().rstrip())
deque = []

for _ in range(n):
    data = stdin.readline().rstrip().split()
    command = data[0]

    if command == "push_front":
        deque.insert(0, data[1])
    elif command == "push_back":
        deque.append(data[1])
    elif command == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif command == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(deque))
    elif command == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif command == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
