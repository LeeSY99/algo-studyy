
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev = None

class Linkedlist:
    def __init__(self, new_node):
        self.head=new_node
        self.tail=new_node
        self.cur_node = new_node
        self.count=1

    def insert_front(self, node):
        if self.cur_node == self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.count +=1
            return
        self.cur_node.prev.next = node
        node.prev = self.cur_node.prev
        node.next = self.cur_node
        self.cur_node.prev=node
        self.count +=1
        

    def insert_back(self,node):
        if self.cur_node == self.tail:
            self.tail.next= node
            node.prev = self.tail
            self.tail=node
            self.count+=1
            return
        self.cur_node.next.prev = node
        node.next = self.cur_node.next
        self.cur_node.next= node
        node.prev = self.cur_node
        self.count +=1
        

    def change_prev(self):
        if self.cur_node.prev:
            self.cur_node=self.cur_node.prev
    
    def change_next(self):
        if self.cur_node.next:
            self.cur_node=self.cur_node.next

    
s_init = input()
new = Node(s_init)
my_list = Linkedlist(new)

n = int(input())

for _ in range(n):
    dir, *word = input().split()
    dir = int(dir)
    if dir == 1:
        new_node = Node(word[0])
        my_list.insert_front(new_node)
    elif dir == 2:
        new_node = Node(word[0])
        my_list.insert_back(new_node)
    elif dir == 3:
        my_list.change_prev()
    elif dir == 4:
        my_list.change_next()

    a = '(Null)' if my_list.cur_node.prev is None else my_list.cur_node.prev.data
    b = '(Null)' if my_list.cur_node is None else my_list.cur_node.data
    c = '(Null)' if my_list.cur_node.next is None else my_list.cur_node.next.data
    print(a,b,c)
    