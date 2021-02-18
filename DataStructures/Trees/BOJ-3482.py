from collections import deque
from copy import deepcopy
from sys import stdin


def bfs(pos):
    global laby, c, r

    q = deque()
    q.append(pos)

    laby[pos[0]][pos[1]] = 0
    rpos = [0, 0]
    result = 0

    while q:
        qx, qy = q.popleft()

        for x, y in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = qx + x, qy + y
            if (0 <= nx <= r) and (0 <= ny <= c):
                if laby[nx][ny] == '.':
                    laby[nx][ny] = laby[qx][qy] + 1
                    q.append([nx, ny])
                    if laby[nx][ny] > result:
                        result = laby[nx][ny]
                        rpos = [nx, ny]

    return rpos, result


t = int(stdin.readline().strip())

for tt in range(t):
    c, r = map(int, stdin.readline().strip().split())
    laby = [[0] * c for i in range(r)]
    start = [0, 0]

    for i in range(r):
        laby[i] = list(stdin.readline().strip())
        if start == [0, 0] and '.' in laby[i]:
            start = [i, laby[i].index('.')]

    temp = deepcopy(laby)
    fpos, f = bfs(start)

    laby = temp
    spos, s = bfs(fpos)

    print("Maximum rope length is {}.".format(s))
