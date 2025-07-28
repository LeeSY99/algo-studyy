n, k = map(int, input().split())

nums = [[0]*(n+1)]
for _ in range(n):
    a = [0]
    a.extend(list(map(int, input().split())))
    nums.append(a)



prefix_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + nums[i][j]

# for a in prefix_sum:
#     print(*a)
max_sum = 0
for i in range(1, n-k+2):
    for j in range(1, n-k+2):
        ei,ej = i+k-1, j+k-1
        m_sum = prefix_sum[ei][ej] - prefix_sum[i-1][ej] - prefix_sum[ei][j-1] + prefix_sum[i-1][j-1]
        max_sum = max(max_sum, m_sum)

print(max_sum)

