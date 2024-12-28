from collections import deque

class Queue:
    def __init__(self):
        self.dq=deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        if self.empty():
            raise Exception('queue is empty')
        return self.dq.popleft()

    def front(self):
        if self.empty():
            raise Exception('queue is empty')
        return self.dq[0]

n = int(input())
queue = Queue()

for _ in range(n):
    dir = input().split()

    if dir[0] == 'push':
        queue.push(int(dir[1]))
    elif dir[0] == 'empty':
        print(int(queue.empty()))
    elif dir[0] == 'size':
        print(queue.size())
    elif dir[0] == 'pop':
        print(queue.pop())
    elif dir[0] == 'front':
        print(queue.front())