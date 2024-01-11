n=int(input())

nums=list(map(int,input().split()))

max_count=0
for k in range(1,101):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if (nums[j]-k) == (k-nums[i]):
                count+=1
    max_count=max(max_count,count)

print(max_count)