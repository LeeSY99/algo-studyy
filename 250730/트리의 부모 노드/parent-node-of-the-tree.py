n = int(input())

class Node:
    def __init__(self,i):
        self.num = i
        self.parent = None

    def connect(self, other):
        self.parent = other

nodes = [None] + [Node(i) for i in range(1,n+1)]

# print(nodes)
for _ in range(n-1):
    p, c = map(int, input().split())
    nodes[c].connect(nodes[p])

for i in range(2,n+1):
    print(nodes[i].parent.num)
