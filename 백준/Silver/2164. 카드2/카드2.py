n = int(input())

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push_back(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1

    def pop_front(self):
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            next_head = self.head.next
            self.head.next.prev = None
            self.head.next = None
            self.head = next_head
        self.count -= 1
        return node

mylist = LinkedList()
for i in range(1, n+1):
    mylist.push_back(Node(i))

stage = 1
while mylist.count != 1:
    if stage%2 == 1:
        mylist.pop_front()
    else:
        front = mylist.pop_front()
        mylist.push_back(front)
    stage += 1

print(mylist.head.num)
