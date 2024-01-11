x,y=map(int,input().split())

max_sum=0
for i in range(x,y+1):
    summ=0
    for l in range(len(str(i))):
        summ+=int(str(i)[l])
    max_sum=max(max_sum,summ)

print(max_sum)