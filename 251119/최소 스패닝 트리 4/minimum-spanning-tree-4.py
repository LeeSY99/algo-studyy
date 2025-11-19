n,m = map(int, input().split())

t = [0] + list(input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key = lambda x: x[2])

def union(a,b):
    A = find(a)
    B = find(b)
    if A==B:
        return
    uf[A] = b

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

uf = [i for i in range(n+1)]

ans = 0
for a,b,v in edges:
    if t[a] == t[b]:
        continue
    if find(a) == find(b):
        continue
    union(a,b)
    ans += v


print(ans)