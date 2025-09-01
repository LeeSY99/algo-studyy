n,k = map(int, input().split())

q = int(input())

class Book:
    def __init__(self,num):
        self.num = num
        self.next = None
        self.prev = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_back(self,node):
        if self.count == 0:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count+=1

    def add_front(self,node):
        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.count+=1

    def pop_back(self):
        if self.count == 1:
            target = self.tail 
            self.head = None
            self.tail = None

        else:
            target = self.tail
            self.tail = self.tail.prev
            self.tail.next = None

        target.prev= None
        target.next = None
        self.count-=1
        return target

    def pop_front(self):
        if self.count == 1:
            target = self.head 
            self.head = None
            self.tail = None

        else:
            target = self.head
            self.head = self.head.next
            self.head.prev = None

        target.prev = None
        target.next = None
        self.count-=1
        return target

def connect_3(i,j):
    if j.count == 0:
        j.head = i.head
        j.tail = i.tail
    else:
        j.head.prev = i.tail
        i.tail.next = j.head

        j.head = i.head
    j.count += i.count

    i.head = None
    i.tail = None
    i.count = 0
     
def connect_4(i,j):
    if j.count == 0:
        j.head = i.head
        j.tail = i.tail
    else:
        j.tail.next = i.head
        i.head.prev = j.tail
        j.tail = i.tail
    j.count += i.count

    i.head = None
    i.tail = None
    i.count = 0

    
book_club = [Linked_list() for _ in range(k+1)]

for i in range(1,n+1):
    book = Book(i)
    book_club[1].add_back(book)
for _ in range(q):
    # print(_,'turn')
    # for i in range(1,k+1):
    #     bc_i = book_club[i]
    #     print(bc_i.count, end = ' ')
    # print()
    cmd, i, j = map(int, input().split())
    if cmd == 1:
        bc_i = book_club[i]
        bc_j = book_club[j]

        if bc_i.count == 0:
            continue
        book = bc_i.pop_front()
        bc_j.add_back(book)

    elif cmd == 2:
        bc_i = book_club[i]
        bc_j = book_club[j]
        if bc_i.count == 0:
            continue
        
        book = bc_i.pop_back()
        bc_j.add_front(book)

    elif cmd == 3:
        bc_i = book_club[i]
        bc_j = book_club[j]
        if bc_i.count == 0 or i==j:
            continue
        connect_3(bc_i,bc_j)

    elif cmd == 4:
        bc_i = book_club[i]
        bc_j = book_club[j]
        if bc_i.count == 0 or i==j:
            continue
        connect_4(bc_i,bc_j)
    

for i in range(1,k+1):
    bc_i = book_club[i]
    print(bc_i.count, end = ' ')

    now = bc_i.head
    while now:
        print(now.num, end = ' ')
        now = now.next

    print()


