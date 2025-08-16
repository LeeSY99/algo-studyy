n,m = map(int, input().split())
start = [0]
end = [0]
beauty = [0]

for _ in range(n):
    s,e,v = map(int, input().split())
    start.append(s)
    end.append(e)
    beauty.append(v)

#dp[i][j] i번째날까지 고려, 마지막 옷 j번 -> 만족도

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        dp[i][j] = float('-inf')

for j in range(n+1):
    if start[j] == 1:
        dp[1][j] = 0

for i in range(2,m+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            #i-1번째 날에 k번 옷을 입은 경우
            #k번 옷이 i-1번째 날에 입을 수 있어야 함
            if start[k] <= i-1 <= end[k] and start[j] <= i <=end[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(beauty[j]-beauty[k]))


ans = max(dp[m][1:n+1])
print(ans)