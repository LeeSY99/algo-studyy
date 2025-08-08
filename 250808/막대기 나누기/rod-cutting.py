n = int(input())
value = [0] + list(map(int, input().split()))

#dp[i] : 길이 i인 막대기를 이용해 얻는 최대 수익

dp = [0] * (n+1)

for i in range(1,n+1):
    #마지막으로 길이가 j 인 막대기를 사용한 경우
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + value[j])

print(dp[n])