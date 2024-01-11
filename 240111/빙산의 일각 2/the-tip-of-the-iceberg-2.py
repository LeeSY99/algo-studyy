n=int(input())

heights=[int(input()) for _ in range(n)]

max_count=0
for h in range(1,1001):
    up=False
    count=0
    for height in heights:
        if height>h and up==False:
            count+=1
            up=True
        if height<=h:
            up=False
    max_count=max(max_count,count)

print(max_count)