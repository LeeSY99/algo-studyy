n=int(input())

dp=[0]*(n+1)
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2] #i-1번째에서 나머지 칸: 1가지 가능

print(dp[n] % 10007)
