import sys

n = int(sys.stdin.readline().rstrip())
tree = {}

for _ in range(n):
    root, left, right = sys.stdin.readline().rstrip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def order(root):
    if root != '.':
        order(tree[root][0])
        print(root, end='')
        order(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
order('A')
print()
postorder('A')