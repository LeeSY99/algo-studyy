class Stack:
    def __init__(self):
        self.items=[]

    def push(self,e):
        self.items.append(e)

    def size(self):
        return len(self.items)

    def empty(self):
        return int(not self.items)

    def top(self):
        if self.empty():
            raise Exception("stack is empty")
        return self.items[-1]

    def pop(self):
        if self.empty():
            raise Exception("stack is empty")
        return self.items.pop()

stack=Stack()

n=int(input())
for _ in range(n):
    dir = input().split()
    if dir[0] == 'push':
        stack.push(int(dir[1]))
    elif dir[0] == 'size':
        print(stack.size())
    elif dir[0] == 'empty':
        print(stack.empty())
    elif dir[0] == 'top':
        print(stack.top())
    elif dir[0] == 'pop':
        print(stack.pop())