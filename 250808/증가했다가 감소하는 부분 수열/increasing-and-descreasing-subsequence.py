''' n개의 숫자 가장 긴 증가-감소 부분 수열 길이'''

n = int(input())
num = list(map(int, input().split()))

''' dp[i][0] i번째 수에서 증가하고 잇음
    dp[i][1] i번째 수에서 감소하고 잇음'''
dp = [[1,1] for _ in range(n)]

# dp[0][0] = 1
# dp[0][1] = 1
# print(dp)

for i in range(1,n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif num[j] > num[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1)

# for d in dp:
#     print(*d)
# print('-----------')

ans = 0
for d in dp:
    ans = max(ans, d[0])
    ans = max(ans, d[1])

print(ans)
