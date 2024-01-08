n,k=map(int,input().split())

bombs=[]
for _ in range(n):
    number=int(input())
    bombs.append(number)

# def in_range(number):
#     return number<n and number>=0

# boom=[]
# for i in range(n):
#     for j in range(i-k,i+k+1):
#         if in_range(j) and i!=j:
#             if bombs[i]==bombs[j]:
#                 boom.append(bombs[i])
# if len(boom)==0:
#     print(-1)
# else:
#     print(max(boom))
ans=-1
for i in range(n):
    for j in range(i+1,n):
        if i-j>k:
            break
        
        if bombs[i] != bombs[j]:
            continue
        
        ans=max(ans,bombs[i])

print(ans)