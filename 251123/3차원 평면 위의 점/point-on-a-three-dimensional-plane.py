n = int(input())
points = [tuple(list(map(int, input().split()))) for _ in range(n)]
points.sort()

uf = [i for i in range(n)]
def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    uf[A] = B

def find(x):
    if uf[x] ==x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

edges = []
def push(i, j):
    x1,y1,z1 = points[i]
    x2,y2,z2 = points[j]
    dist = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
    edges.append((i,j,dist))

points.sort(key=lambda x: x[0])
for i in range(n-1):
    push(i,i+1)

points.sort(key=lambda x: x[1])
for i in range(n-1):
    push(i,i+1)

points.sort(key=lambda x:x[2])
for i in range(n-1):
    push(i,i+1)

edges.sort(key = lambda x: x[2])
ans = 0
for i, j, dist in edges:
    if find(i) == find(j):
        continue
    ans += dist
    union(i,j)
print(ans)