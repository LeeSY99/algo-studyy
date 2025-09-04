n,k = map(int, input().split())

grid = [[0] * (n+1)]
for _ in range(n):
    arr = [0] + list(map(int, input().split()))
    grid.append(arr)

prefix_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + grid[i][j]

ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        sum_all = 0
        for r in range(i-k, i+k+1):
            c = k - abs(i-r)
            if 1<= r <=n:
                sum_all += prefix_sum[r][min(j+c,n)] - prefix_sum[r][max(j-c-1, 0)]

        ans = max(ans, sum_all)

print(ans)
