n,k,u,d = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
def in_range(r,c):
    return 0<=r<n and 0<=c<n

drs, dcs = [-1,1,0,0],[0,0,-1,1]
visited = [[0]*n for _ in range(n)]

sizes=[]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            q = deque([(i,j)])
            visited[i][j] = 1
            size = 0
            
            while q:
                r, c = q.popleft()
                size+=1
                for dr, dc in zip(drs,dcs):
                    nr, nc = r+dr, c+dc
                    if in_range(nr,nc) and not visited[nr][nc]:
                        diff = abs(city[r][c] - city[nr][nc])
                        if u<= diff <=d:
                            visited[nr][nc] = 1
                            q.append((nr,nc))
            sizes.append(size)

sizes.sort(reverse=True)
ans = sum(sizes[:k])
print(ans)
    