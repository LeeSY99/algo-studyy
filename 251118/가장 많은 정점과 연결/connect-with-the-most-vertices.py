n,m,k = map(int, input().split())

nums = [0] + list(map(int, input().split()))

def union(a,b):
    A = find(a)
    B = find(b)
    if A==B: return
    if nums[A] < nums[B]:
        A,B = B,A
    parent[A] = B

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

parent = [i for i in range(n+1)] 
for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)

visited = [False] * (n+1)
cost_list = []
for i in range(1,n+1):
    I = find(i)
    if visited[I]:
        continue
    visited[I] = True
    cost_list.append(nums[I])

cost_list.sort()

ans = 0
for i in range(1, len(cost_list)):
    ans += cost_list[0] + cost_list[i]

if ans > k:
    print('NO')
else:
    print(ans)