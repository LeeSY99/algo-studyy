import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[1] * n for _ in range(n)]

dis,djs = [0,0,-1,1],[1,-1,0,0]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

cells = []

for i in range(n):
    for j in range(n):
        cells.append((grid[i][j],i,j))

cells.sort()

for _,i,j in cells:
    for di, dj in zip(dis,djs):
        ni, nj = i+di, j+dj
        if in_range(ni,nj) and grid[ni][nj] > grid[i][j]:
            dp[ni][nj] = max(dp[ni][nj], dp[i][j]+1)


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])
print(ans)






# -----------------------dfs-------------------------
# ans = 0
# from collections import deque
# q = deque()

# def dfs(i,j):
#     if dp[i][j] != -1:
#         return dp[i][j]
    
#     dp[i][j] = 1
#     for di, dj in zip(dis,djs):
#         ni, nj = i+di, j+dj
#         if in_range(ni,nj) and grid[ni][nj] > grid[i][j]:
#             dp[i][j] = max(dp[i][j], dfs(ni,nj)+1)
#     return dp[i][j]

# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dfs(i, j))
        
        
# print(ans)
# for d in dp:
#     print(*d)
