n,m = map(int, input().split())


def union(a,b):
    A = find(a)
    B = find(b)
    parent[A] = B

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

parent = [i for i in range(n+1)]

ans = 0
for i in range(1,m+1):
    a,b = map(int, input().split())
    if find(a) == find(b):
        ans = i
        break
    union(a, b)

if ans != 0:
    print(ans)
else:
    print('happy')

