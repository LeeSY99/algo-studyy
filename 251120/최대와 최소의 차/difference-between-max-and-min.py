n,m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(lambda x:-x[2])

uf_min = [i for i in range(n+1)]
uf_max = [i for i in range(n+1)]

def union(a,b,uf):
    A = find(a,uf)
    B = find(b,uf)
    if A == B:
        return
    uf[A] = B

def find(x, uf):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x], uf)
    return uf[x]

min_k = 0
for a,b,t in edges:
    if find(a,uf_min) == find(b, uf_min):
        continue
    union(a,b,uf_min)
    if t == 0:
        min_k += 1

max_k = 0
for i in range(m-1,-1,-1):
    a,b,t = edges[i]
    if find(a,uf_max) == find(b,uf_max):
        continue
    union(a,b,uf_max)
    if t == 0:
        max_k += 1

print(max_k**2 - min_k**2)