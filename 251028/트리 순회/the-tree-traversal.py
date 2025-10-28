n = int(input())
class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

nodes = {}

for _ in range(n):
    n, l, r = input().split()
    if n not in nodes:
        node = Node(n)
        nodes[n] = node
    else:
        node = nodes[n]
    if l != '.':
        if l not in nodes:
            left = Node(l)
        else:
            left = nodes[l]
        node.left = left
        nodes[l] = left
    if r != '.':
        if r not in nodes:
            right = Node(r)
        else:
            right = nodes[r]
        node.right = right
        nodes[r] = right


def preorder(x):
    if x == None:
        return
    print(x.id, end = '')
    preorder(x.left)
    preorder(x.right)

def inorder(x):
    if x == None:
        return
    inorder(x.left)
    print(x.id, end = '')
    inorder(x.right)

def postorder(x):
    if x == None:
        return
    postorder(x.left)
    postorder(x.right)
    print(x.id, end = '')

preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])
print()