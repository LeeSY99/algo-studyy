T = int(input())

#dp[i][j]: j열에서 i행의 스티커를 선택한 경우의 최대 개수
def calc():
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = grid[0][0]
    dp[1][0] = grid[1][0]

    if n >= 2:
        dp[0][1] = dp[1][0] + grid[0][1]
        dp[1][1] = dp[0][0] + grid[1][1]

    for j in range(2,n):
        dp[0][j] = max(dp[1][j-1] + grid[0][j],
                       max(dp[0][j-2], dp[1][j-2]) + grid[0][j])
        dp[1][j] = max(dp[0][j - 1]+ grid[1][j],
                       max(dp[0][j-2], dp[1][j-2]) + grid[1][j])

    return max(dp[0][n-1], dp[1][n-1])


for _ in range(T):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]
    print(calc())



