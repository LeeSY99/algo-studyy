n, k = map(int, input().split())
# candy = [0] * 1000001
# for _ in range(n):
#     a, x = map(int, input().split())
#     candy[x] += a

# sum_val = sum(candy[: 1+k+k ])
# ans = sum_val
# for c in range(1+k, 1000001 - k):
#     i = c-k
#     j = c+k
#     sum_val -= candy[i-1]
#     sum_val += candy[j]
#     ans = max(ans, sum_val)
    

candies = []
for _ in range(n):
    cnt, x = map(int, input().split())
    candies.append((x,cnt))

candies.sort()
ans = 0 
total_val = 0
j = 0
for i in range(n):
    while j<n and candies[j][0] - candies[i][0] <= 2*k:
        total_val += candies[j][1]
        j+=1
    ans = max(ans, total_val)
    total_val -= candies[i][1]
print(ans)

