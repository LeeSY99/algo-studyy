nums=list(map(int,input().split()))

nums.sort()
def is_possible(a,b,c,d):
    available=[a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]
    available.sort()
    if available==nums:
        return True
    else:
        return False
                

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            for l in range(k+1,len(nums)):
                a,b,c,d=nums[i],nums[j],nums[k],nums[l]
                if is_possible(a,b,c,d):
                    print(a,b,c,d)
                    quit()