n,k=map(int,input().split())

nums=[int(input()) for _ in range(n)]

max_select=0
for i in range(n):
    selected=[]
    standard_num=nums[i]
    selected.append(standard_num)
    for j in range(n):
        if i==j:
            continue
        if nums[j] in range(standard_num,standard_num+k+1):
            selected.append(nums[j])
    max_select=max(max_select,len(selected))

print(max_select)