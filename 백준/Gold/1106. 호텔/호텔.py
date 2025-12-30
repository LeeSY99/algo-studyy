c,n = map(int, input().split())
costs = []
for _ in range(n):
    a,b = map(int, input().split())
    costs.append((a,b))

max_get = max(g for _, g in costs)
limit = c + max_get

#dp[i]: i명을 모으는 데 드는 최소 비용
dp = [float('inf')] * (limit + 1)
dp[0] = 0

for i in range(limit + 1):
    if dp[i] == float('inf'):
        continue
    for cost, get in costs:
        ni = min(limit, i + get)
        if dp[ni] > dp[i] + cost:
            dp[ni] = dp[i] + cost

print(min(dp[c:]))