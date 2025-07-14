n = int(input())
d = dict()

def add(k,v):
    d[k] = v

def remove(k):
    d.pop(k)

def find(k):
    if k in d:
        print(d[k])
    else:
        print(None)

for _ in range(n):
    direction = list(input().split())
    if direction[0] == 'add':
        add(int(direction[1]), int(direction[2]))
    elif direction[0] == 'remove':
        remove(int(direction[1]))
    elif direction[0] == 'find':
        find(int(direction[1]))

