arr, k = input().split()
k = int(k)
n = len(arr)

j = 0
count = {}
ans = 0
for i in range(n):
    while j<n and len(count) <= k:
        if arr[j] not in count and len(count) == k:
            break
        if arr[j] in count:
            count[arr[j]] +=1
        else:
            count[arr[j]] = 1
        j+=1
    
    ans = max(ans, sum(count.values()))
    if count[arr[i]] == 1:
        count.pop(arr[i])
    else:
        count[arr[i]] -= 1
  

print(ans)