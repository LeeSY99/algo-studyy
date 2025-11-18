n,m = map(int, input().split())
import sys
sys.setrecursionlimit(100000)
parent = [i for i in range(n+1)]
ans = n

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]



for _ in range(m):
    a,b = map(int, input().split())

    while True:
        a = find(a)

        if a>=b:
            break
        
        parent[a] = a+1
        a = a+1
        ans -= 1
    
    print(ans)
    