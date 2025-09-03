N,M,Q = map(int, input().split())
class Person:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None

#id로 노드
people = [None] * (N+1)
#각 라인별 헤드와 테일
head = [None] * (M+1)
tail = [None] * (M+1)

line_num = [0] * (N+1)

for i in range(1,M+1):
    p_count, *line = map(int, input().split())
    for p_num in line:
        person = Person(p_num)
        people[p_num] = person
        line_num[p_num] = i
        if head[i] == None:
            head[i] = person
            tail[i] = person
        else:
            tail[i].next = person
            person.prev = tail[i]
            tail[i] = person
def pop(a):
    a_node = people[a] 
    line_num_a = line_num[a]
    if line_num_a == 0:
        return
    #a가 빠져나옴
    if a_node == head[line_num_a]:
        head[line_num_a] = a_node.next

    if a_node == tail[line_num_a]:
        tail[line_num_a] = a_node.prev
    
    if a_node.prev is not None:
        a_node.prev.next = a_node.next
    if a_node.next is not None:
        a_node.next.prev = a_node.prev

    a_node.next = None
    a_node.prev = None
    line_num[a] = 0

def cmd1(a, b):
    a_node = people[a] 
    line_num_a = line_num[a]
    b_node = people[b]
    line_num_b = line_num[b]
    pop(a)

    #b앞으로 들어감
    if b_node == head[line_num_b]:
        head[line_num_b].prev = a_node
        a_node.next = head[line_num_b]
        head[line_num_b] = a_node
    else:
        b_node.prev.next = a_node
        a_node.prev = b_node.prev
        a_node.next = b_node
        b_node.prev = a_node

    line_num[a] = line_num_b
    
def cmd3(a,b,c):
    a_node = people[a] 
    line_num_a = line_num[a]
    b_node = people[b]
    line_num_b = line_num[b]

    if a_node == head[line_num_a]:
        head[line_num_a] = b_node.next
    if b_node == tail[line_num_b]:
        tail[line_num_b] = a_node.prev
    
    if a_node.prev is not None:
        a_node.prev.next = b_node.next
    if b_node.next is not None:
        b_node.next.prev = a_node.prev
    a_node.prev = None
    b_node.next = None

    ##c와 연결
    c_node = people[c]
    line_num_c = line_num[c]

    if c_node == head[line_num_c]:
        b_node.next = head[line_num_c]
        head[line_num_c].prev = b_node
        head[line_num_c] = a_node
    else:
        a_node.prev = c_node.prev
        c_node.prev.next = a_node
        b_node.next = c_node
        c_node.prev = b_node

    n_node = a_node
    while n_node != c_node:
        line_num[n_node.num] = line_num_c
        n_node = n_node.next


for _ in range(Q):
    cmd, *rem = map(int, input().split())
    if cmd == 1:
        a, b = rem[0], rem[1]
        cmd1(a, b)
    elif cmd == 2:
        a = rem[0]
        pop(a)
    elif cmd == 3:
        a,b,c = rem[0], rem[1], rem[2]
        cmd3(a,b,c)

for i in range(1,M+1):
    node = head[i]
    if node == None:
        print(-1)
        continue
    while node:
        print(node.num, end = ' ')
        node = node.next
    print()