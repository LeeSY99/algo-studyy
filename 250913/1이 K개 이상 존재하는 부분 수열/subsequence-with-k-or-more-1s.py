
n, k = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
count = 0


ans = float('inf')
for i in range(n):
    while j<n and count < k:
        if arr[j] == 1:
            count+=1
        j+=1
    
    if count == k:
        ans = min(ans, j-i)
    if arr[i] == 1:
        count-=1

if ans == float('inf'):
    ans = -1
print(ans)