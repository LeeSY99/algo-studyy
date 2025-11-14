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

parent = set(parent)
# print(parent)
count += len(parent) - 2
print(count)