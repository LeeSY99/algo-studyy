n = int(input())
points = []

for idx in range(n):
    x, y, z = map(int, input().split())
    # (x, y, z, 원래 인덱스)
    points.append((x, y, z, idx))

uf = [i for i in range(n)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(a, b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    uf[A] = B

edges = []

def push(i, j):
    x1, y1, z1, id1 = points[i]
    x2, y2, z2, id2 = points[j]
    dist = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
    # 간선은 "원래 인덱스 id1, id2" 기준으로 저장
    edges.append((id1, id2, dist))

# x 기준
points.sort(key=lambda x: x[0])
for i in range(n-1):
    push(i, i+1)

# y 기준
points.sort(key=lambda x: x[1])
for i in range(n-1):
    push(i, i+1)

# z 기준
points.sort(key=lambda x: x[2])
for i in range(n-1):
    push(i, i+1)

edges.sort(key=lambda x: x[2])

ans = 0
for a, b, dist in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    ans += dist

print(ans)
