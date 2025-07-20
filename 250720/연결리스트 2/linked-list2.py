class Node:
    def __init__(self, id, data):
        self.id = id
        self.data=data
        self.next=None
        self.prev = None

def pop_node(node):
    if node.prev is not None:
        node.prev.next= node.next
    if node.next is not None:
        node.next.prev = node.prev
    node.prev=None
    node.next=None


def insert_prev(j_node,i_node):
    if i_node.prev is None:
        j_node.next = i_node
        i_node.prev = j_node
    else:
        i_node.prev.next = j_node
        j_node.prev = i_node.prev
        j_node.next = i_node
        i_node.prev = j_node


def insert_next(j_node,i_node):
    if i_node.next is None:
        i_node.next = j_node
        j_node.prev = i_node
    else:
        i_node.next.prev = j_node
        j_node.next = i_node.next
        i_node.prev = j_node
        j_node.next = i_node



n = int(input())
nodes = {}
for i in range(1,n+1):
    new_node = Node(i,i)
    nodes[i] = new_node

q = int(input())
for _ in range(q):
    dir, *num = map(int, input().split())
    if dir == 1:
        node = nodes[num[0]]
        pop_node(node)
    elif dir == 2:
        i, j = num[0], num[1]
        i_node = nodes[i]
        j_node = nodes[j]
        insert_prev(j_node,i_node)
    elif dir == 3:
        i, j = num[0], num[1]
        i_node = nodes[i]
        j_node = nodes[j]
        insert_next(j_node,i_node)
    elif dir == 4:
        i = num[0]
        i_node = nodes[i]
        a = 0 if i_node.prev is None else i_node.prev.id
        c = 0 if i_node.next is None else i_node.next.id
        print(a,c)

for i in range(1,n+1):
    node = nodes[i]
    a = 0 if node.next is None else node.next.data
    print(a, end = ' ')


