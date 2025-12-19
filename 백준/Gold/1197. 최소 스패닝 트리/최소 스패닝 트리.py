# from functools import cmp_to_key
import sys
sys.setrecursionlimit(100000)
v,e = map(int, input().split())

edges = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

edges.sort(key= lambda x: x[2])
parent = [i for i in range(v+1)]
def union(a,b):
    A = find(a)
    B = find(b)
    parent[A] = B

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

ans = 0
for a,b,c in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    ans += c

print(ans)