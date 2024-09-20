n=int(input())
nums=list(map(int,input().split()))

odd,even=0,0
for num in nums:
    if num%2==0:
        even+=1
    else:
        odd+=1

count=0
ans=0

if odd>=even:
    ans+=even*2
    odd-=even
    even=0
else:
    ans+=odd*2
    even-=odd
    odd=0

if odd==0 and even>=1:
    ans+=1
elif odd%3==0:
    ans+=odd//3*2
elif odd%3==1:
    ans+=odd//3*2-1
else:
    ans+=odd//3*2+1

print(ans)