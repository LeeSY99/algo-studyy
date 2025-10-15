n,m = map(int, input().split())
v1, v2, e = map(int, input().split())

dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    dist[a][b] =  c
    dist[b][a] = c
for i in range(1,n+1):
    dist[i][i] = 0
# for d in dist:
#     print(*d)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

# print('0---=')
# for d in dist:
#     print(*d)
ans = dist[v1][e] + dist[v2][e]
# print(ans)
for k in range(1, n+1):
    new_dist = dist[v1][k] + dist[v2][k] + dist[k][e]
    ans = min(ans, new_dist)
if ans == float('inf'):
    ans = -1
print(ans)