n, k  = map(int, input().split())

nums= [list(map(int, input().split())) for _ in range(n)]

ans = 0

from collections import deque

dis, djs = [0,1,0,-1],[1,0,-1,0]
def in_range(i,j):
    return 0<=i<n and 0<=j<n

def bfs(q):
    count = 0
    while q:
        cur_i, cur_j = q.popleft()
        count+=1
        for di, dj in zip(dis, djs):
            ni, nj = cur_i+di, cur_j+dj
            if in_range(ni, nj) and not visited[ni][nj] and not nums[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni,nj))
    return count

visited = [[0]*n for _ in range(n)]

for _ in range(k):
    ri, ci = map(int, input().split())
    q = deque()
    q.append((ri-1, ci-1))    
    visited[ri-1][ci-1] = 1
    bfs(q)
    
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            ans+=1
print(ans)
