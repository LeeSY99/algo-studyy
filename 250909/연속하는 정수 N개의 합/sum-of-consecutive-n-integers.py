n,m = map(int, input().split())

arr = list(map(int, input().split()))

j = 0
ans = 0
sum_val = 0
for i in range(n):
    while j < n and sum_val < m:
        sum_val += arr[j]
        j += 1
    
    if sum_val == m:
        ans += 1
    sum_val -= arr[i]

print(ans)