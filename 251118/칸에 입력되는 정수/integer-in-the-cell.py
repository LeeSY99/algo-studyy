n = int(input())
m = int(input())


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

ans = m
parent = [i for i in range(n+1)]
for i in range(1, m+1):
    a = int(input())
    A = find(a)
    if A == 0:
        ans = i-1
        break
    Y = find(A-1)
    parent[A] = Y

print(ans)
    