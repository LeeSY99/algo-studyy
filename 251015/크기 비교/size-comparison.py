n,m = map(int, input().split())
bigger = [[False] * (n+1) for _ in range(n+1)]
smaller = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    bigger[a][b] = True
    smaller[b][a] = True
    # compare[b][a] = True

for i in range(1,n+1):
    bigger[i][i] = True
    smaller[i][i] = True


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if bigger[i][k] and bigger[k][j]:
                bigger[i][j] = True
            if smaller[i][k] and smaller[k][j]:
                smaller[i][j] = True

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if i == j:
            continue
        if not (bigger[i][j] or smaller[i][j]):
            cnt+=1
    print(cnt)