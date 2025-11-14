n,m = map(int, input().split())

parent = [i for i in range(n+1)]

def union(a,b):
    A = find(a)
    B = find(b)
    parent[B] = A

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

count = 0
for _ in range(m):
    a,b = map(int, input().split())
    if find(a) == find(b):
        count+=1
    else:
        union(a,b)


for i in range(2,n+1):
    if find(1) != find(i):
        union(1, i)
        count+= 1

print(count)