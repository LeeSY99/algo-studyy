n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = {}
ans = 0
for n in nums:
    d = k-n
    if d in count:
        ans += count[d]
    
    if n in count:
        count[n] +=1
    else: count[n] = 1

print(ans)