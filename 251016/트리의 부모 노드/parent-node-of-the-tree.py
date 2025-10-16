n = int(input())
class Node:
    def __init__(self, num):
        self.num = num
        # self.child = []
        self.parent = None

nodes = [None] * (n+1)
for i in range(1,n+1):
    node = Node(i)
    nodes[i] = node

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[b].parent = a

for i in range(2,n+1):
    print(nodes[i].parent)
