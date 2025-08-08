n, m = map(int, input().split())
coins = list(map(int, input().split()))

#dp[i] = i원을 거슬러줄 최대 동전의 개수
dp = [0] * (m+1)

for i in range(1,m+1):
    for coin in coins:
        if i-coin >=0:
            dp[i] = max(dp[i], dp[i-coin] + 1)

print(dp[m])