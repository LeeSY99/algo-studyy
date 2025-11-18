n,m,k = map(int, input().split())

nums = [0] + list(map(int, input().split()))

def union(a,b):
    A = find(a)
    B = find(b)

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

start = find(1)
cost = 0
for i in range(1,n+1):
    I = find(i)
    if I == start:
        continue
    # print(parent)
    # print(start, I)
    # print('------------')
    union(start, I)
    cost += (nums[start] + nums[I])
    start = find(1)


if cost > k:
    print('NO')
else:
    print(cost)