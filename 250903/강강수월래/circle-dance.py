N,M,Q = map(int, input().split())

class Student:
    def __init__(self,num):
        self.num = num
        self.prev = None
        self.next = None

stu_to_node = {}

for _ in range(M):
    count, *stus = map(int, input().split())
    head = None
    tail = None
    for j in range(count):
        student = Student(stus[j])
        stu_to_node[stus[j]] = student
        if j == 0:
            head = student
            tail = student
        else:
            tail.next = student
            student.prev = tail
            tail = student
    tail.next = head
    head.prev = tail

def connect(s,e):
    if s:
        s.next = e
    if e:
        e.prev = s

def split_circle(a,b):
    temp = a.prev
    a.prev.next = b
    b.prev.next = a
    a.prev = b.prev
    b.prev = temp
    
for _ in range(Q):
    cmd, *rem = map(int, input().split())
    if cmd == 1:
        a,b = rem[0], rem[1]
        connect(stu_to_node[b].prev, stu_to_node[a].next)
        connect(stu_to_node[a], stu_to_node[b])
    elif cmd == 2:
        a,b = rem[0], rem[1]
        split_circle(stu_to_node[a],stu_to_node[b])
    elif cmd == 3:
        a = rem[0]
        cur = stu_to_node[a].next
        min_val = cur.num
        min_node = cur

        while cur != stu_to_node[a]:
            if cur.num < min_val:
                min_val = cur.num
                min_node = cur
            cur = cur.next

        cur = min_node
        while cur != min_node.next:
            print(cur.num, end = ' ')
            cur = cur.prev
        print(cur.num, end = ' ')
