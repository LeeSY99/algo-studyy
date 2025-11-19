n,m = map(int, input().split())

edges = []
for _ in range(m):
    a,b,v = map(int, input().split())
    edges.append((a,b,v))

edges.sort(key = lambda x : x[2])

uf = [i for i in range(n+1)]
def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    uf[A] = B

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


ans = 0
for a,b,v in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    ans += v

print(ans)
    