n=int(input())
nums=list(map(int,input().split()))

max_num,max_index=0,0
for i in range(n):
    if nums[i]>max_num:
        max_num=nums[i]
        max_index=i

if max_index==n-1:
    print(0)
else:  
    print(max_index+1)