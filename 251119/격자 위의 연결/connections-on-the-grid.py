n,m = map(int, input().split())

edges = []
uf = [i for i in range(n*m)]
for i in range(n):
    values = list(map(int, input().split()))
    j = 0
    for v in values:
        edges.append((m*i + j, m*i+j+1, v))
        j+=1

for i in range(n-1):
    values = list(map(int, input().split()))
    j = 0
    for v in values:
        edges.append((m*i+j, m*(i+1)+j, v))
        j+=1

edges.sort(key = lambda x: x[2])
def union(a,b):
    A=find(a)
    B=find(b)
    if A==B: return
    uf[A]=B

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