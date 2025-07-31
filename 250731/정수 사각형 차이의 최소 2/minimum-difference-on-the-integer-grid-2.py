n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

import sys
dp = [
    [0] * n
    for _ in range(n)
]



def initialize():
    global dp
    dp = [[sys.maxsize] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], grid[i][0])
        dp[0][i] = max(dp[0][i-1], grid[0][i])

def solve(lower_bound):
    for i in range(n):
        for j in range(n):
            if grid[i][j]<lower_bound:
                grid[i][j] = sys.maxsize
    
    initialize()

    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])
    
    return dp[n-1][n-1]

ans = sys.maxsize
for lower_bound in range(1, 101):
    upper_bound = solve(lower_bound)
    if upper_bound == sys.maxsize:
        continue

    ans = min(ans, upper_bound-lower_bound)

print(ans)
# max_dp = [[0] * n for _ in range(n)]
# min_dp = [[0] * n for _ in range(n)]
# max_dp[0][0] = grid[0][0]
# min_dp[0][0] = grid[0][0]

# for i in range(1,n):
#     min_dp[0][i] = min(min_dp[0][i-1], grid[0][i])
#     min_dp[i][0] = min(min_dp[i-1][0], grid[i][0])

#     max_dp[0][i] = max(max_dp[0][i-1], grid[0][i])
#     max_dp[i][0] = max(max_dp[i-1][0], grid[i][0])

# # for i in range(1,n):
# #     for j in range(1,n):
# #         min_dp[i][j] = min(max(min_dp[i-1][j], min_dp[i][j-1]), grid[i][j])
# #         max_dp[i][j] = max(min(max_dp[i-1][j], max_dp[i][j-1]), grid[i][j])

# dp = [[0] * n for _ in range(n)]

# for i in range(1, n):
#     dp[0][i] = min(max_dp[0][i-1]-min_dp[0][i-1], max_dp[0][i]-min_dp[0][i])
#     dp[i][0] = min(max_dp[i-1][0]-min_dp[i-1][0], max_dp[i][0]-min_dp[i][0])

# for i in range(1,n):
#     for j in range(1,n):
#         a = max_dp[i][j-1]-min_dp[i][j-1]
#         b = max_dp[i-1][j]-min_dp[i-1][j]
#         c = max_dp[i][j] - min_dp[i][j]
#         dp[i][j] = min(a,b,c)
# def pr(a):
#     for a_ in a:
#         print(*a_)
#     print('-------')

# pr(min_dp)
# pr(max_dp)
# pr(dp)
# print(dp[n-1][n-1])