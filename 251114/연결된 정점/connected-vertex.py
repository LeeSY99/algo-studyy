n,m = map(int, input().split())


def union(a,b):
    A = find(a)
    B = find(b)
    if A==B:
        return
    if count[A] < count[B]:
        A,B = B,A
    
    parent[B] = A
    count[A] += count[B]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

count = [1] * (n+1)
parent = [i for i in range(n+1)]

for _ in range(m):
    cmd, *var = input().split()
    if cmd == 'x':
        a, b = int(var[0]), int(var[1])
        union(a,b)
        
    elif cmd == 'y':
        a = int(var[0])
        p = find(a)
        print(count[p])
