n=int(input())

nums=[list(map(int,input().split())) for _ in range(n)]

ok=False
for x in range(1,5001):
    for i in range(n):
        ai,bi=nums[i][0],nums[i][1]
        num=x*(2**(i+1))
        if ai<=num<=bi:
            if i==n-1:
                ok=True
        else:
            break
    if ok:
        print(x)
        break