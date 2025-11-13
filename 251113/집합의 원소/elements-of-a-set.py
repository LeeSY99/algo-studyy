n,m = map(int, input().split())
import sys
sys.setrecursionlimit(100000)
parent = [i for i in range(n+1)]

def union(a,b):
    A = find(a)
    B = find(b)
    parent[A] = b

def find(x):
    if parent[x] == x:
        return x
    root = find(parent[x])
    parent[x] = root
    return root

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a,b)
    elif cmd == 1:
        print(int(parent[a] == parent[b]))