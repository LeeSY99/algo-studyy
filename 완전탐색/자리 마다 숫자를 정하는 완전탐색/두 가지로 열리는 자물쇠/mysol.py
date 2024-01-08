n=int(input())

a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())

count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):#연결된 지역은 차이가 n-2보다 큼
            if (abs(a1-i)<=2 or abs(a1-i)>= n-2) and\
            (abs(b1-j)<=2 or abs(b1-j)>=n-2) and\
            (abs(c1-k)<=2 or abs(c1-k)>=n-2):
                count+=1

            elif (abs(a2-i)<=2 or abs(a2-i)>= n-2) and\
            (abs(b2-j)<=2 or abs(b2-j)>=n-2) and\
            (abs(c2-k)<=2 or abs(c2-k)>=n-2):
                count+=1

print(count)

