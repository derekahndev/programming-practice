def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    root = inorder.index(preorder[0])

    left_in = inorder[0:root]
    left_pre = preorder[1:1 + len(left_in)]
    postorder(left_pre, left_in)

    right_in = inorder[root + 1:]
    right_pre = preorder[len(left_pre) + 1:]
    postorder(right_pre, right_in)

    print(preorder[0], end=' ')


t = int(input())

for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    postorder(preorder, inorder)
    print()
