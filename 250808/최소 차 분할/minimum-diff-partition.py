n = int(input())

nums = [0] + list(map(int, input().split()))

#dp[i] : a그룹에 들어갓을 떄 차이

dp = [0] * (n+1)
num_sum = sum(nums)


#dp[i][j] : i번쨰 수만 고려 고른 수의 합을 j로 만들 수 잇으면 true/ false

dp = [[0] * (num_sum+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(num_sum+1):
        #1) i를 선택
        if j >= nums[i] and dp[i-1][j-nums[i]] :
            dp[i][j] = 1
        #2) i를 선택하지 않음
        if dp[i-1][j]:
            dp[i][j] = 1

import sys
ans = sys.maxsize

for i in range(1,num_sum):
    if dp[n][i]:
        ans = min(ans, abs(i - (num_sum - i)))

print(ans)
