n=int(input())
nums=list(map(int,input().split()))

max_num,max_index=0,0
for i in range(n):
    if nums[i]>max_num:
        max_num=nums[i]
        max_index=i

print(max_index+1)