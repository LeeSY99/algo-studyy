n = int(input())
parent = {}
size = {}

def make(x):
    if x not in parent:
        parent[x] = x
        size[x] = 1
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    make(a)
    make(b)
    A = find(a)
    B = find(b)
    if A==B: return 
    if size[A] < size[B]:
        A,B = B,A
    parent[B]=A
    size[A] += size[B]

    
for _ in range(n):
    a,b = map(int, input().split())
    union(a,b)
    A = find(a)
    print(size[A])