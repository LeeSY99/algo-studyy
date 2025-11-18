import sys
n = int(input())

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.empty():
            return -1
        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def empty(self):
        return self.size() == 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.arr[-1]

stack = Stack()

for _ in range(n):
    cmd, *x = sys.stdin.readline().split()
    if cmd == 'push':
        stack.push(int(x[0]))
    elif cmd == 'pop':
        print(stack.pop())
    elif cmd == 'size':
        print(stack.size())
    elif cmd == 'empty':
        print(int(stack.empty()))
    elif cmd == 'top':
        print(stack.top())




