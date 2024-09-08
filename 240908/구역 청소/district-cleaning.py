a,b =map(int,input().split())
c,d=map(int,input().split())

# intersect=1
# if b < c or d < a:
#     intersect=0

# if intersect:
#     ans= (max(a,c)-min(a,c))+(max(b,d)-min)
    
# else:
#     ans=(d-c)+(b-a)
    
ans=max(b,d)-min(a,c)
print(ans)