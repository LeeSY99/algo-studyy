n,m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(lambda x: x[2])

uf = [i for i in range(n+1)]


def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    uf[A] = b

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

ans = 0

cnt = n
for a,b,v in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    cnt -= 1
    ans += v
    if cnt == 2:
        break

print(ans)