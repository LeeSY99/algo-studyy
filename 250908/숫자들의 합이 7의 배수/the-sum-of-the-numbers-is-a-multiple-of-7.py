n = int(input())
nums = [int(input()) for _ in range(n)]

ans = 0
prefix_sum = [0] * n
prefix_sum[0] = nums[0]
for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]


for i in range(n):
    for j in range(1,i):
        if (prefix_sum[i] -prefix_sum[j-1]) % 7 == 0:
            ans = max(ans, i-j+1)
            break

print(ans)