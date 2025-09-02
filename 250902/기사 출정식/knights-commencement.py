n,m = map(int, input().split())
knights = list(map(int, input().split()))
class Knight:
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
        if self.count == 0:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1
        self.tail.next = self.head
        self.head.prev = self.tail

    def pop(self,node):
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            node.next = None

        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

        self.count -= 1
        self.tail.next = self.head
        self.head.prev = self.tail

knight_list = [[] for _ in range(10**9+1)]
linked_knight_list = LinkedList()
for k in knights:
    kn = Knight(k)
    knight_list[k] = kn
    linked_knight_list.push_back(kn)

for _ in range(m):
    num = int(input())
    knight_node = knight_list[num]
    print( knight_node.next.num, knight_node.prev.num,)
    linked_knight_list.pop(knight_node)

