''' 1~p 점은 빨강/ 단방향 이동
A -> B로 이동 경로 내 적어도 빨강이 포함되어야 함
빨강을 지나는 가짓수, 가능한 루트의  최소 비용의 합'''

n,m,p,q = map(int, input().split())
dist = [[float('inf')] * (n+1)  for _ in range(n+1)]
for i in range(1,n+1):
    dist[i][i] = 0
for _ in range(m):
    u,v,c = map(int, input().split())
    dist[u][v] = min(dist[u][v], c)

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k]+dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k]+dist[k][j]

cnt = 0
cost = 0
for _ in range(q):
    i, j = map(int, input().split())
    dist_ij = float('inf')
    for k in range(1, p+1):
        dist_ij = min(dist_ij, dist[i][k]+dist[k][j])
    if dist_ij == float('inf'):
        continue
    cnt+=1
    cost += dist[i][j]

print(cnt)
print(cost)