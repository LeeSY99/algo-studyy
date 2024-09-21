nums=list(map(int,input().split()))

nums.sort()

a=nums[0]
b=nums[1]
c=nums[2]
d=nums[-1]-a-b-c

print(a,b,c,d)