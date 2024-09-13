n=int(input())
nums=list(map(int,input().split()))
nums.sort()
# print(nums)

plus_start=0
zero_start=-1

for i in range(n):
    if nums[i]>0:
        plus_start=i
        break
for i in range(n):
    if nums[i]==0:
        zero_start=i
        break
# print(plus_start,zero_start)

#0포함
ans=0

#양수3
for i in range(plus_start,n):
    for j in range(i+1,n):
        for k in range(j+1):
            ans=max(ans,nums[i]*nums[j]*nums[k])


#양수1, 음수2

if zero_start==-1:
    for i in range(0,plus_start):
        for j in range(i+1,plus_start):
            for k in range(plus_start,n):
                ans=max(ans,nums[i]*nums[j]*nums[k])
else:
    for i in range(0,zero_start):
            for j in range(i+1,zero_start):
                for k in range(plus_start,n):
                    ans=max(ans,nums[i]*nums[j]*nums[k])

print(ans)