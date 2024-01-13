a,b,c=map(int,input().split())

max_num=0
for i in range(c):
    for j in range(c):
        num=a*i+b*j
        if num<=c:
            max_num=max(max_num,num)
        else:
            break

print(max_num)