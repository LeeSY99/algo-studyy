import math
n,m = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        x1,y1 = points[i]
        x2,y2 = points[j]
        v = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append((i+1,j+1, v))

uf = [i for i in range(n+1)]
def union(a,b):
    A = find(a)
    B = find(b)
    if A==B:
        return
    uf[A] = B

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)

edges.sort(key = lambda x: x[2])

ans = 0
for a,b,v in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    ans += v
print(f'{ans:.2f}')