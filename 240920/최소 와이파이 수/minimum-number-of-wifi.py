n,m=map(int,input().split())

live = list(map(int,input().split()))

# if m==0:
#     ans=sum(live)
# else:
ans=0
index=0
while(1):
    if live[index]==1:
        ans+=1
        index+=2*m+1
    else:
        index+=1
    if index>=n:
        break


print(int(ans))