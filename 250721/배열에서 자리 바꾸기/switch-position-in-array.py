n = int(input())
q = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def connect(s,e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def change(a,b,c,d):
    after_prevA = c.prev
    after_nextB = d.next
    after_prevC = a.prev
    after_nextD = b.next

    #b와 c가 붙어있는 경우
    if b.next == c:
        after_prevA = d
        after_nextD = a
    #d와 a가 붙어있는 경우
    if d.next == a:
        after_nextB = c
        after_prevC = b

    connect(after_prevA, a)
    connect(b, after_nextB)
    connect(after_prevC, c)
    connect(d, after_nextD)

nodes = [None] * (n+1)
for i in range(1,n+1):
    new_node = Node(i)
    nodes[i] = new_node

for i in range(1,n):
    connect(nodes[i], nodes[i+1])

for _ in range(q):
    a,b,c,d = map(int, input().split())
    change(nodes[a],nodes[b],nodes[c],nodes[d])

cur = nodes[1]
while cur.prev:
    cur = cur.prev

while cur:
    print(cur.data, end = ' ')
    cur = cur.next
    



    