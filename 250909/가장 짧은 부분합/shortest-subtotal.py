N, S = map(int, input().split())

ans = float('inf')
arr = list(map(int, input().split()))

j = 0
sum_val = 0
for i in range(N):
    while j<N and sum_val < S:
        sum_val += arr[j]
        j += 1
    
    if sum_val < S: break
    
    ans = min(ans, j-i)
    sum_val -= arr[i]
        
if ans == float('inf'):
    ans = -1
print(ans)

