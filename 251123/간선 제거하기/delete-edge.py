n,m = map(int, input().split())

edges = []
all_dist = 0
for _ in range(m):
    a,b,dist = map(int, input().split())
    edges.append((a,b,dist))
    all_dist += dist

def union(a,b):
    A= find(a)
    B = find(b)
    if A==B:
        return
    uf[A] = B

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

uf = [i for i in range(n+1)]
min_dist = 0
edges.sort(key = lambda x: x[2])

for a,b, dist in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    min_dist += dist

print(all_dist - min_dist)