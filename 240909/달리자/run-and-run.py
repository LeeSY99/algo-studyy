n=int(input())

ai=list(map(int,input().split()))
bi=list(map(int,input().split()))

people=0
count=0
for i in range(n-1):
    if ai[i]>bi[i]:
        count += (ai[i]-bi[i])
        ai[i+1] += (ai[i]-bi[i])

print(count)