n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[1] * n for _ in range(n)]

dis,djs = [0,0,-1,1],[1,-1,0,0]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

ans = 0
def bfs(i,j):
    global ans
    for di, dj in zip(dis, djs):
            ni, nj = i+di, j+dj
            if in_range(ni,nj) and grid[ni][nj] > grid[i][j]:
                dp[ni][nj] = max(dp[i][j] + 1, dp[ni][nj])
                ans = max(ans,dp[ni][nj])
                bfs(ni,nj)

for i in range(n):
    for j in range(n):
        bfs(i,j)
        
        
print(ans)
# for d in dp:
#     print(*d)
