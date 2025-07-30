n = int(input())

stair = [0] *(n+1)

for i in range(1,n+1):
    if i==1:
        continue
    if i==2:
        stair[i]=1
    elif i==3:
        stair[i]=1

    else:
        stair[i] = stair[i-2] + stair[i-3]

# print(stair)
print(stair[n]%10007)