n = int(input())
edges = [[] for _ in range(n+1)]
import sys
sys.setrecursionlimit(100000)

for _ in range(n-1):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)



ans = 0
stack = [(1,0,0)]
while stack:
    x,p,d = stack.pop()
    is_leaf = True
    for y in edges[x]:
        if y == p:
            continue
        is_leaf = False
        stack.append((y,x,d+1))
    if is_leaf:
        ans += d

print(ans%2)
