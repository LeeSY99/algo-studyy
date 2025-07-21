import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            return
        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            return
        return -self.items[0]

    
n = int(input())
my_q = PriorityQueue()

for _ in range(n):
    to_do, *num = input().split()
    if to_do == 'push':
        item = int(num[0])
        my_q.push(item)
    elif to_do == 'pop':
        print(my_q.pop())
    elif to_do == 'size':
        print(my_q.size())
    elif to_do == 'empty':
        print(int(my_q.empty()))
    elif to_do == 'top':
        print(my_q.top())
