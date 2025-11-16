n,m = map(int, input().split())

edges = []

def union(x,y):
    X = find(x)
    Y = find(y)
    if X==Y: return
    if count[X] < count[Y]:
        X,Y = Y,X
    
    count[X] += count[Y]
    parent[Y] = X

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

count = [1] * (n+1)
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    # edges.append((a,b))
    union(a,b)

a,b,k = map(int, input().split())
A = find(a)
B = find(b)

ans = 0
visited = set([A])
node_count = []

for i in range(1,n+1):
    I = find(i)
    if I in visited:
        continue
    if I == B:
        continue
    visited.add(I)
    node_count.append(count[I])

node_count.sort(reverse=True)
# print(node_count)
# print(count)
# print(count[A] , sum(node_count[:k]))
print(count[A] + sum(node_count[:k]))
    
            
    