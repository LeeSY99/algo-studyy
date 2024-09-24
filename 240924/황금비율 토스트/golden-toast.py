class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.END = Node(-1)                # 구현의 편의를 위해 dummy 값을 넣어놓고 시작합니다.
        self.head = self.END
        self.tail = self.END

    def push_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        
        self.head.prev=new_node
        self.head=new_node
        new_node.prev=None

    def push_back(self,data):
        if self.begin() == self.end():     # 만약 리스트가 비어있다면
            self.push_front(data)

        else:
            new_node=Node(data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node 
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self,node):
        next_node=node.next

        if node==self.begin():
            tmp=self.head
            tmp.next.prev=None
            self.head=tmp.next
            tmp.next=None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev 
            node.prev = None
            node.next = None 
        return next_node
        
    def insert(self,node,data):
        if node == self.end():    #맨 뒤에 삽입
            self.push_back(data)
        elif node==self.begin(): 
            self.push_front(data)
        else:
            new_node=Node(data)
            new_node.prev = node.prev 
            new_node.next = node           # 새로운 노드의 next값을 node로 하고
            node.prev.next = new_node      # node의 prev의 next값을 새로운 노드로 변경하고
            node.prev = new_node

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

    def print(self,node):
        return node.data


my_list=DoubleLinkedList()
n,m=map(int,input().split())
in_str=input()

for i in range(n):
    my_list.push_back(in_str[i])

now_node=my_list.end()
for _ in range(m):
    direction=input().split()
    if direction[0]=='L':
        if now_node!=my_list.begin():
            now_node=now_node.prev
    elif direction[0]=='R':
        if now_node!=my_list.end():
            now_node=now_node.next
    elif direction[0]=='D':
        if now_node!=my_list.end():
            my_list.erase(now_node)
    elif direction[0]=='P':
        my_list.insert(now_node,direction[1])
        

it = my_list.begin()
while it != my_list.end():
    print(it.data, end='')
    it=it.next