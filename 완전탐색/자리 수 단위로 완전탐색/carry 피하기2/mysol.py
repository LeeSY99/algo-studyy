n=int(input())

nums=[input() for _ in range(n)]

max_sum=-1
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            overflow=False
            num_len=max(len(nums[i]),len(nums[j]),len(nums[k]))
            a,b,c=int(nums[i]),int(nums[j]),int(nums[k])
            for z in range(1,num_len+1):
                if a%(10)+b%(10)+c%(10) >=10:
                    overflow=True
                    break
                else:
                    a=a//10
                    b=b//10
                    c=c//10
            if not overflow:
                num_sum=int(nums[i])+int(nums[j])+int(nums[k])
                max_sum=max(max_sum,num_sum)

print(max_sum)