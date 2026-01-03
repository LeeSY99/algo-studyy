n,m = map(int, input().split())

uf = [i for i in range(n)]
count = [1] * (n)

def union(x,y):
    X = find(x)
    Y = find(y)
    if X == Y:
        return
    if count[X] < count[Y]:
        X,Y = Y,X

    uf[Y] = X
    count[X] += count[Y]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

ans = 0
for i in range(1,m+1):
    a,b = map(int, input().split())
    if find(a) == find(b):
        ans = i
        break
    union(a,b)
# print(uf)
print(ans)