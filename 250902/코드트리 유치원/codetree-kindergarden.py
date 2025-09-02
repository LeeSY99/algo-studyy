''' 놀이기구 줄 -> 랜덤으로
처음엔 1번학생

반복
1) a번학생 뒤에 b명의 학생을 세움
2) a번 학생 앞에 b명의 학생을 세움
3) a번 학생 앞과 뒤 학생'''

Q = int(input())
class Student:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push_back(self, node):
        if self.count == 0:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def push_1(self, node, new):
        if node == self.tail:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        else:
            new.next = node.next
            new.prev = node
            node.next.prev = new
            node.next = new

        self.count += 1

    def push_2(self, node, new):
        if node == self.head:
            self.head.prev = new
            new.next = self.head
            self.head = new

        else:
            new.next = node
            new.prev = node.prev
            node.prev.next = new
            node.prev = new

        self.count += 1
            

line = Linkedlist()
st1 = Student(1)
line.push_back(st1)
students = [[] for _ in range(100001)]
students[1] = st1
num = 2
for _ in range(Q):
    cmd, *rem = map(int, input().split())
    if cmd == 1:
        a,b = rem[0],rem[1]
        node = students[a]
        for n in range(num+b-1, num-1, -1):
            new = Student(n)
            students[n] = new
            line.push_1(node,new)

        num += b    

    elif cmd == 2:
        a,b = rem[0],rem[1]
        node = students[a]
        for n in range(num, num+b):
            new = Student(n)
            students[n] = new
            line.push_2(node,new)
        num += b    
        
        
    else:
        a = rem[0]
        front = students[a].prev
        back = students[a].next

        if not front or not back:
            print(-1)
        else:
            print(front.num, back.num)

    # node = line.head
    # while node:
    #     print(node.num, end = ' -> ')
    #     node = node.next