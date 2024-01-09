import copy
n,b=map(int,input().split())
prices=[]
for _ in range(n):
    p,s=map(int,input().split())
    prices.append([p,s])

present_available=0
for i in range(n):
    price=copy.deepcopy(prices)
    price[i][0]=price[i][0]//2
    price.sort(key=lambda x: sum(x))
    now=0
    student=0
    for j in range(n):
        now=now + price[j][0] + price[j][1]
        student+=1
        if now>b:
            student-=1
            break
    present_available=max(present_available,student)

print(present_available)