n,k = map(int, input().split())

nums = list(map(int, input().split()))

count = {}

ans = 0
for i in range(n):
    n1 = nums[i] 

    for j in range(i+1,n):
        n2 = nums[j]
        diff = k - n1 - n2
        if diff in count:
            ans += count[diff]

    if n1 in count:
        count[n1] += 1
    else:
        count[n1] = 1

    
         
        

print(ans)