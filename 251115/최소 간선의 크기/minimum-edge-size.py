n,m = map(int, input().split())

a,b = map(int, input().split())

def union(x,y):
    X = find(x)
    Y = find(y)

    parent[Y] = X

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

satis = [0] * (n+1)
parent = [i for i in range(n+1)]

graph = []
for _ in range(m):
    x,y,s = map(int, input().split())
    graph.append((x,y,s))

graph.sort(key = lambda x: -x[2])

for x,y,d in graph:
    union(x,y)
    A = find(a)
    B = find(b)

    if A==B:
        print(d)
        break

    