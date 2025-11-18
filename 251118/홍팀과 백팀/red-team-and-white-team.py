n,m = map(int, input().split())

def union(a,b):
    A = find(a)
    B = find(b)
    if A == B: return
    parent[A] = B


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

parent = [i for i in range(2*n+1)]
ans = 1
for _ in range(m):
    a,b = map(int, input().split())
    if find(a) == find(b):
        ans = 0
        break
    union(a,b+n)
    union(b,a+n)

print(ans)
