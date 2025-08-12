''' 카드 무작위 양의 양수 

더미의 맨 위 카드를 비교

둘 중 하나 선택
1) 카드 대결
    서로 카드 비교
    자신이 작으면 카드에 적힌만큼 점수 얻고 버림
    같으면 둘다 버림

2) 카드 버리기
    둘중 하나 소진 시까지 계속 얻은 점수의 합이 최종점수'''

#dp[i][j] 상대 카드 i, 남우카드 j번째 -> 남우가 얻는 최대 점수

n = int(input())

dp = [[-1] * (n+1) for _ in range(n+1)]
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        if a[i+1] < b[j+1]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        if a[i+1] > b[j+1]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + b[j+1])

        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

ans = 0
# for d in dp:
#     print(*d)
for i in range(n + 1):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])

print(ans)