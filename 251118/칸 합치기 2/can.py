n,m = map(int, input().split())

parent = [i for i in range(n+1)]
nxt = [i for i in range(n + 2)]
visited = [False] * (n+1)
comp_cnt = n 

def union(a,b):
    global comp_cnt
    A = find(a)
    B = find(b)
    if A == B: return
    parent[A] = B
    comp_cnt -= 1

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def get_next(x):
    if nxt[x] == x:
        return x
    nxt[x] = get_next(nxt[x])
    return nxt[x]

for _ in range(m):
    a,b = map(int, input().split())

    i = get_next(a)
    while i<b:
        union(i, i+1)
        nxt[i] = get_next(i+1)
        i = nxt[i]
    print(comp_cnt)
    