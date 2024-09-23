class Node:

    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.node_num=0

    def push_front(self, data):
        new_node = Node(data)
        new_node.next=self.head

        if self.head !=None:
            self.head.prev=new_node
            self.head=new_node
            new_node.prev=None
        else:
            self.head=new_node
            self.tail=new_node
            new_node.prev=None
        self.node_num +=1

    def push_back(self,data):
        new_node = Node(data)
        new_node.prev=self.tail

        if self.tail != None:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=None
        else:
            self.tail=new_node
            self.head=new_node
            new_node.next=None
        self.node_num+=1

    def pop_front(self):
        if self.head==None:
            print('list is empty')

        elif self.head.next==None: #노드가 1개
            temp=self.head
            self.head=None
            self.tail=None
            self.node_num=0
            return temp.data

        else:
            temp=self.head
            temp.next.prev=None
            self.head=temp.next
            temp.next=None
            self.node_num-=1
            return temp.data

    def pop_back(self):
        if self.tail==None:
            print('list is empty')

        elif self.tail.prev==None: #노드가 1개
            temp=self.tail
            self.head=None
            self.tail=None
            self.node_num=0
            return temp.data

        else:
            temp=self.tail
            temp.prev.next=None
            self.tail=temp.prev
            temp.prev=None
            self.node_num-=1
            return temp.data
    
    def size(self):
        return self.node_num
    
    def empty(self):
        return int(self.node_num==0)

    def front(self):
        if self.head==None:
            print('list is empty')
        else:
            return self.head.data   

    def back(self):
        if self.tail==None:
            print('list is empty')
        else:
            return self.tail.data

n=int(input())
my_list=DoubleLinkedList()

for _ in range(n):
    direction=input().split()
    if direction[0]=='push_front':
        my_list.push_front(direction[1])
    elif direction[0]=='push_back':
        my_list.push_back(direction[1])
    elif direction[0]=='pop_front':
        print(my_list.pop_front())
    elif direction[0]=='pop_back':
        print(my_list.pop_back())
    elif direction[0]=='size':
        print(my_list.size())
    elif direction[0]=='empty':
        print(my_list.empty())
    elif direction[0]=='front':
        print(my_list.front())
    elif direction[0]=='back':
        print(my_list.back())