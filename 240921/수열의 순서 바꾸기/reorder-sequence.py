n=int(input())
nums=list(map(int,input().split()))

ans=0
for i in range(n-1):
    ok=True
    for j in range(i,n-1):
        if nums[j]>nums[j+1]:
            ok=False
            ans+=1
    if ok:
        break

print(ans)