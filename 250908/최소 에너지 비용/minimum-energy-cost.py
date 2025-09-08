n = int(input())
energy = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = [0] * n
#i번째까지 충전 가장 비용이 작은 곳
min_cost[0] = cost[0]
for i in range(1,n):
    min_cost[i] = min(min_cost[i-1], cost[i])
# print(min_cost)
ans = 0
for i in range(n-1):
    ans += min_cost[i] * energy[i]

print(ans)



