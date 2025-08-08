
n = int(input())

nums = [[0] * (n+1)]
for _ in range(n):
    a = [0] + list(map(int, input().split()))
    nums.append(a)


prefix_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + nums[i][j]

def get_sum(x1,y1,x2,y2):
    return prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]

def get_max_area(x1,x2):
    dp = [0] * (n+1)
    for y in range(1,n+1):
        value = get_sum(x1,y,x2,y)
        dp[y] = max(value, dp[y-1] + value)

    max_area = -sys.maxsize
    for y in range(1,n+1):
        max_area = max(max_area, dp[y])

    return max_area

import sys
ans = -sys.maxsize
for i in range(1,n+1): # 시작 행
    for j in range(i,n+1): # 끝 행
        ans = max(ans, get_max_area(i,j))
print(ans)
# for p in prefix_sum:
#     print(*p)