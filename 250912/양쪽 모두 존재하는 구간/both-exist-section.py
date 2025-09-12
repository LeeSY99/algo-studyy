n,m = map(int, input().split())
arr = list(map(int, input().split()))

inner = [0] * (m+1)
outer = [0] * (m+1)
for a in arr:
    outer[a] += 1


inner_count = 0
outer_count = 0
for o in outer:
    if o:
        outer_count += 1

j = 0
ans = float('inf')
for i in range(n):
    while j<n and inner_count < m:
        if inner[arr[j]] == 0:
            inner_count += 1
        inner[arr[j]] += 1
        
        outer[arr[j]] -= 1
        if outer[arr[j]] == 0:
            outer_count -= 1
        j+=1
        # print(inner_count, inner)
        # print(outer_count,outer)
        # print('----')    
    if inner_count == m and outer_count == m:
        ans = min(ans, j-i)
    inner[arr[i]] -= 1
    if inner[arr[i]] == 0:
        inner_count -= 1
    
    if outer[arr[i]] == 0:
        outer_count += 1
    outer[arr[i]] += 1 

if ans == float('inf'):
    ans = -1
print(ans)