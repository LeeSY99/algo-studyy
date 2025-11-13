n,m,k = map(int, input().split())

graph = [[] for _ in range(n+1)]


def union(x,y):
    X = find(x)
    Y = find(y)
    parent[X] = Y

def find(x):
    if parent[x] == x:
        return x
    root = find(parent[x])
    parent[x] = root
    return root


parent = [i for i in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    union(x,y)


path = list(map(int, input().split()))
ans = 1
for i in range(k-1):
    if find(path[i]) != find(path[i+1]):
        ans = 0

print(ans)