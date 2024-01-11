x,y=map(int,input().split())

interest_count=0
def interest(number):
    nums=[0]*10
    ok1=False
    ok2=False
    for n in str(number):
        nums[int(n)]+=1
    for n in nums:
        if n==1:
            ok1=True
        if n==len(str(number))-1:
            ok2=True
    return ok1 and ok2

for i in range(x,y+1):
    if interest(i):
        interest_count+=1

print(interest_count)