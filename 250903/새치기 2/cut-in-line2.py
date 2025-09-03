N,M,Q = map(int, input().split())

class Person:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

name_to_node = {}
people = list(input().split())
head = [None] * (M+1)
tail = [None] * (M+1)
line_num = {}

for i, name in enumerate(people, 1):
    X = N//M

    line = i/X
    if line > i//X:
        line = i//X + 1
    else:
        line = i//X
    
    person = Person(name)
    name_to_node[name] = person
    if head[line] == None:
        head[line] = person
        tail[line] = person
    else:
        tail[line].next = person
        person.prev = tail[line]
        tail[line] = person
    
    line_num[name] = line

def connect(s,e):
    if s:
        s.next = e
    if e:
        e.prev = s

def node_pop(node):
    l = line_num[node.name]
    if l == 0:
        return
    if node == head[l]:
        head[l] = node.next

    if node == tail[l]:
        tail[l] = node.prev

    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev

    node.next = node.prev = None
    line_num[node.name] = 0

def move_many(a,b,c):
    a_node = name_to_node[a]
    b_node = name_to_node[b]
    line_num_b = line_num[b_node.name]

    if a_node == head[line_num_b]:
        head[line_num_b] = b_node.next
    if b_node == tail[line_num_b]:
        tail[line_num_b] = a_node.prev

    connect(a_node.prev, b_node.next)

    c_node = name_to_node[c]
    line_num_c = line_num[c_node.name]

    connect(c_node.prev, a_node)
    connect(b_node, c_node)
    if head[line_num_c] == c_node:
        head[line_num_c] = a_node

    cur = a_node
    while cur != c_node.next:
        line_num[cur.name] = line_num_c
        cur = cur.next

for _ in range(Q):
    cmd, *rem = input().split()
    if cmd == '1':
        a, b = rem[0], rem[1]
        a_node = name_to_node[a]
        b_node = name_to_node[b]
        line_num_b = line_num[b_node.name]

        node_pop(a_node)
        connect(b_node.prev, a_node)
        connect(a_node, b_node)

        if b_node == head[line_num_b]:
            head[line_num_b] = a_node
        line_num[a_node.name] = line_num_b
    elif cmd == '2':
        a = rem[0]
        a_node = name_to_node[a]
        node_pop(a_node)
    else:
        a,b,c = rem[0], rem[1], rem[2]
        move_many(a,b,c)

for i in range(1,M+1):
    cur = head[i]
    if cur == None:
        print(-1)
        continue

    while cur:
        print(cur.name, end = ' ')
        cur = cur.next
    print()

