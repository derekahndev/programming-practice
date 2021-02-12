import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.depth = 0
        self.num = 0


def inorder(node, depth):
    global num
    if node == -1:
        return
    inorder(a[node].left, depth + 1)
    a[node].depth = depth
    num += 1
    a[node].num = num
    inorder(a[node].right, depth + 1)


n = int(sys.stdin.readline().strip())

a = [Node() for _ in range(n + 1)]
left_val = [0] * (n + 1)
right_val = [0] * (n + 1)
check = [False] * (n + 1)
num = 0

for _ in range(n):
    c1, c2, c3 = map(int, sys.stdin.readline().strip().split())
    a[c1].left = c2
    a[c1].right = c3

    if c2 != -1:
        check[c2] = True
    if c3 != -1:
        check[c3] = True

root = 0

for i in range(1, n + 1):
    if not check[i]:
        root = i

inorder(root, 1)

max_depth = 0

for i in range(1, n + 1):
    depth = a[i].depth
    num = a[i].num

    if left_val[depth] == 0:
        left_val[depth] = num
    else:
        left_val[depth] = min(left_val[depth], num)

    right_val[depth] = max(right_val[depth], num)
    max_depth = max(max_depth, depth)

depth_ans = 0
num_ans = 0

for i in range(1, max_depth + 1):
    if num_ans < right_val[i] - left_val[i] + 1:
        num_ans = right_val[i] - left_val[i] + 1
        depth_ans = i

print(depth_ans, num_ans)
