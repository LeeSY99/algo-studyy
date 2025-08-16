n,m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
p_s = [0] * (n+1)
for i in range(1,n+1):
    p_s[i] = p_s[i-1]+arr[i]

#dp[i][j] = i번쨰 숫자까지 고려 j개의 구간, 최대값

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = float('-inf')
## 구간이 1개일땐 [l,i] -> 구간의 최대값
for i in range(1,n+1):
    for l in range(1,i+1):
        dp[i][1] = max(dp[i][1], p_s[i]-p_s[l-1])

# for j in range(1, m+1):
#     best = float('-inf')
#     #prev : i번째에서 끝나는 새 구간을 붙일때 구간 시작 전까지 최적 구간 합
#     for i in range(1,n+1):
#         if i>=2:
#             prev = dp[i-2][j-1]
#         else:
#             #i가 2보다 작고 j=1이면 앞에 구간이 필요 없으니 0
#             # 아니면 j-1개 구간이 있어야 하는데 불가능
#             prev = 0 if j==1 else float('-inf')
#         best = max(best,prev-p_s[i-1])

#         dp[i][j] = max(dp[i-1][j], p_s[i] + best) 
        
for i in range(1,n+1):
    for j in range(2,m+1):
        #1~l-2 사이의 k 중에 dp[k][j-1]값이 가장 클때의 k값
        max_k = 1
        #j번째로 정한 구간이 [l,i]일때
        #k=1일때 이어질 수 없으므로 l의 최소 3부터 시작
        for l in range(3,i+1):
            dp[i][j] = max(dp[i][j], dp[max_k][j-1] + p_s[i]-p_s[l-1])
            
            #[1,l-2]구간의 k가 기록되어 있음
            #l이 증가해서 그런듯
            #l-1번째 위치 추가 고
            if dp[l-1][j-1] > dp[max_k][j-1]:
                max_k = l -1


ans = max([
    dp[i][m]
    for i in range(1, n + 1)
])
print(ans)
# print(dp[n][m])
# for d in dp:
#     print(*d)
        
