
n = int(input())

nums = [[0] * (n+1)]
for _ in range(n):
    a = [0] + list(map(int, input().split()))
    nums.append(a)


prefix_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + nums[i][j]

import sys
ans = -sys.maxsize
for ei in range(1,n+1):
    for ej in range(1,n+1):
        for si in range(1,ei+1):
            for sj in range(1,ej+1):
                sq_sum = prefix_sum[ei][ej] - prefix_sum[si-1][ej] - prefix_sum[ei][sj-1] + prefix_sum[si-1][sj-1]
                ans = max(ans, sq_sum)
print(ans)
# for p in prefix_sum:
#     print(*p)