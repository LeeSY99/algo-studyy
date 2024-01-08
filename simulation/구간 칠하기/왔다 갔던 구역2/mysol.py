n=int(input())
passed=[0]*2001

now=1000
for _ in range(n):
    x,direction=input().split()
    x=int(x)
    for i in range(x):
        if direction=='R':
            passed[now]+=1
            now+=1
        elif direction=='L':
            now-=1
            passed[now]+=1

count=0
for i in passed:
    if i>=2:
        count+=1

print(count)

