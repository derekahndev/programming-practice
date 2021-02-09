class Node:
    def __init__(self, item, left_child, right_child):
        self.item = item
        self.left_child = left_child
        self.right_child = right_child


def preorder(node):
    print(node.item, end='')
    if node.left_child != '.':
        preorder(tree[node.left_child])
    if node.right_child != '.':
        preorder(tree[node.right_child])


def inorder(node):
    if node.left_child != '.':
        inorder(tree[node.left_child])
    print(node.item, end='')
    if node.right_child != '.':
        inorder(tree[node.right_child])


def postorder(node):
    if node.left_child != '.':
        postorder(tree[node.left_child])
    if node.right_child != '.':
        postorder(tree[node.right_child])
    print(node.item, end='')


n = int(input())
tree = {}

for i in range(n):
    data = input().split()
    tree[data[0]] = Node(item=data[0], left_child=data[1], right_child=data[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
