n = int(input())

lines = []
for _ in range(n):
    x1,x2 = map(int, input().split())
    lines.append((x1,x2))

lines.sort()
dp = [1]*n
dp[0] = 1

for i in range(n):
    for j in range(i):
        if lines[i][0] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1) 

ans= 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)