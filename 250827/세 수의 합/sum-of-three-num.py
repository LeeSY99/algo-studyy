n,k = map(int, input().split())

nums = list(map(int, input().split()))

count = {}

ans = 0
for i in range(n):
    for j in range(i+1,n):
        s = nums[i]+nums[j]
        diff = k-s
        if diff in count:
            ans += count[diff]
        
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

print(ans)