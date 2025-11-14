n = int(input())

parent = [i for i in range(n+1)]

def union(a,b):
    A = find(a)
    B = find(b)

    if A < B:
        A, B = B, A
    
    parent[A] = B

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

for _ in range(n-2):
    a,b = map(int, input().split())
    union(a,b)

first, second = 0,0
for i in range(1,n+1):
    if first == 0:
        first = find(i)
    now = find(i)
    if first != 0 and now != first:
        second = now

# print(parent)
print(first, second)