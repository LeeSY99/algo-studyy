n=int(input())

line = list(input().split())

end=n-1
count=0
while(1):
    if end==0:
        break
    for i in range(end):
        if line[i]>line[i+1]:
            count+=1
            line[i],line[i+1]=line[i+1],line[i]
    end-=1

print(count)