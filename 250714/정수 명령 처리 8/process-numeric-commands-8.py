class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, A):
        new_node = Node(A)
        new_node.next = self.head
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        else:
            self.head.prev = new_node
            self.head = new_node 
            new_node.prev = None
        self.length += 1

    def push_back(self, A):
        new_node = Node(A)
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        self.length+=1

    def pop_front(self):
        if self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.data
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.length -= 1
            return temp.data

    def pop_back(self):
        if self.tail.prev == None:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return temp.data
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.length -= 1
            return temp.data

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data
    
n = int(input())

mylist = DoubleLinkedList()
for _ in range(n):
    direction = list(input().split())
    if direction[0] == 'push_back':
        mylist.push_back(int(direction[1]))
    elif direction[0] == 'push_front':
        mylist.push_front(int(direction[1]))
    elif direction[0] == 'pop_front':
        print(mylist.pop_front())
    elif direction[0] == 'pop_back':
        print(mylist.pop_back())
    elif direction[0] == 'size':
        print(mylist.size())
    elif direction[0] == 'empty':
        print(mylist.empty())
    elif direction[0] == 'front':
        print(mylist.front())
    elif direction[0] == 'back':
        print(mylist.back())

    