n,m=map(int,input().split())

live = list(map(int,input().split()))

ans=n/(2*m+1)
ans=ans+(1 if ans > int(ans) else 0)

print(int(ans))